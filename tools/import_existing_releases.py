"""One-time release migration. Copies published assets, never application Git history."""
import base64,hashlib,json,os,re,tempfile,urllib.request,urllib.parse
from pathlib import Path
SOURCE='ravenridgelights-turtle/TurtleBox-Designer'
TARGET='ravenridgelights-turtle/TurtleBox-Designer-Downloads'
SOURCE_SHA='ad4e6aa74206a56ef25c871fbaa8e90c3571a980'
TARGET_ID=1421548441

def api(path,method='GET',data=None,raw=None):
    host='https://api.github.com'
    url=path if path.startswith('https://') else host+path
    assert urllib.parse.urlparse(url).hostname in ('api.github.com','uploads.github.com')
    headers={'User-Agent':'TurtleBox-release-migration','Accept':'application/vnd.github+json','Authorization':'Bearer '+os.environ['GH_TOKEN'],'X-GitHub-Api-Version':'2022-11-28'}
    body=raw if raw is not None else (json.dumps(data).encode() if data is not None else None)
    if body is not None:headers['Content-Type']='application/octet-stream' if raw is not None else 'application/json'
    with urllib.request.urlopen(urllib.request.Request(url,data=body,headers=headers,method=method),timeout=180) as r:return json.load(r)

def main():
    assert os.environ['GITHUB_REPOSITORY']==TARGET,'This importer runs only in the temporary staging repository.'
    target=api('/repos/'+TARGET);assert target['id']==TARGET_ID and target['visibility']=='public'
    source=api('/repos/'+SOURCE);assert source['id']==1418279475 and source['visibility']=='public'
    head=api('/repos/'+SOURCE+'/git/ref/heads/main');assert head['object']['sha']==SOURCE_SHA,'Source advanced; review the backup before migrating.'
    releases=api('/repos/'+SOURCE+'/releases?per_page=100');releases=[r for r in releases if not r['draft'] and not r['prerelease']]
    assert len(releases)==9 and sum(len(r['assets']) for r in releases)==27
    for r in releases:
        assert re.fullmatch(r'v\d+\.\d+\.\d+',r['tag_name'])
        for a in r['assets']:
            assert a['name'].startswith('TurtleBox-Designer-') and Path(a['name']).name==a['name']
            assert a['digest'].startswith('sha256:')
    ref=api('/repos/'+TARGET+'/git/ref/heads/main');parent=ref['object']['sha'];commit=api('/repos/'+TARGET+'/git/commits/'+parent)
    entries=api('/repos/'+SOURCE+'/git/trees/'+SOURCE_SHA+'?recursive=1')['tree'];changes=[]
    for entry in entries:
        path=entry['path']
        if entry['type']!='blob' or not (path.startswith('docs/releases/') or path=='TurtleBoxDesigner/app/assets/turtle-logo.webp'):continue
        value=api('/repos/'+SOURCE+'/git/blobs/'+entry['sha']);body=base64.b64decode(value['content'])
        if path.endswith('/flyer.html'):body=body.replace(b'../../../TurtleBoxDesigner/app/assets/turtle-logo.webp',b'../../../assets/turtle-logo.webp')
        if path.endswith('turtle-logo.webp'):path='assets/turtle-logo.webp'
        blob=api('/repos/'+TARGET+'/git/blobs','POST',{'content':base64.b64encode(body).decode(),'encoding':'base64'})
        changes.append({'path':path,'type':'blob','mode':'100644','sha':blob['sha']})
    tree=api('/repos/'+TARGET+'/git/trees','POST',{'base_tree':commit['tree']['sha'],'tree':changes})
    added=api('/repos/'+TARGET+'/git/commits','POST',{'message':'Import public release documentation without application source history','parents':[parent],'tree':tree['sha']})
    api('/repos/'+TARGET+'/git/refs/heads/main','PATCH',{'sha':added['sha'],'force':False})
    existing={r['tag_name']:r for r in api('/repos/'+TARGET+'/releases?per_page=100')}
    release_count=asset_count=0
    for original in sorted(releases,key=lambda r:tuple(map(int,r['tag_name'][1:].split('.')))):
        tag=original['tag_name'];current=existing.get(tag)
        if not current:current=api('/repos/'+TARGET+'/releases','POST',{'tag_name':tag,'target_commitish':added['sha'],'name':original['name'],'body':original['body'],'draft':True,'prerelease':False,'make_latest':'false'})
        assets={a['name']:a for a in api('/repos/'+TARGET+'/releases/'+str(current['id']))['assets']}
        for old in original['assets']:
            name=old['name'];found=assets.get(name)
            if found:
                assert found['size']==old['size'] and found['digest']==old['digest'],'Existing asset differs; never overwrite it.'
            else:
                with urllib.request.urlopen(urllib.request.Request(old['browser_download_url'],headers={'User-Agent':'TurtleBox-release-migration'}),timeout=180) as r:content=r.read()
                assert len(content)==old['size'] and 'sha256:'+hashlib.sha256(content).hexdigest()==old['digest']
                upload=current['upload_url'].split('{',1)[0]+'?name='+urllib.parse.quote(name,safe='')
                found=api(upload,'POST',raw=content)
                assert found['digest']==old['digest'] and found['size']==old['size']
            asset_count+=1;print('Verified '+tag+'/'+name,flush=True)
        assert set(assets).issubset({a['name'] for a in original['assets']})
        api('/repos/'+TARGET+'/releases/'+str(current['id']),'PATCH',{'draft':False,'make_latest':'true' if tag=='v1.10.7' else 'false'})
        release_count+=1
    assert api('/repos/'+TARGET+'/releases/latest')['tag_name']=='v1.10.7'
    final=api('/repos/'+TARGET+'/git/trees/'+added['sha']+'?recursive=1')['tree']
    assert not any(e['path'].startswith('TurtleBoxDesigner/') for e in final)
    print(json.dumps({'releases':release_count,'assets':asset_count,'publicSourceHistory':False,'sanitizedCommit':added['sha']}))
if __name__=='__main__':main()
