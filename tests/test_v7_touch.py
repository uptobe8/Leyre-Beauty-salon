from pathlib import Path
from playwright.sync_api import sync_playwright
import re,json
import sys
P=Path(sys.argv[1] if len(sys.argv)>1 else 'Royal_Beauty_Studio_V7_revision_autonomo.html');results=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);pg=b.new_page(viewport={'width':390,'height':844},is_mobile=True,has_touch=True);pg.set_default_timeout(15000);err=[];pg.on('pageerror',lambda e:err.append(str(e)));pg.evaluate("Object.defineProperty(window,'localStorage',{value:{getItem(k){return this[k]??null},setItem(k,v){this[k]=v}}})");html=P.read_text();scripts=re.findall(r'<script>(.*?)</script>',html,re.S);pg.set_content(re.sub(r'<script>.*?</script>','',html,flags=re.S),wait_until='load',timeout=30000)
 for script in scripts:pg.add_script_tag(content=script)
 def c(s):pg.locator(s).first.tap()
 def ev(s):return pg.evaluate(s)
 def check(name,val):
  assert val,name;results.append(name);print('PASS',name,flush=True)
 c('[data-home-mode=hair]');c('#characterConfirm');pg.wait_for_function('BEAUTY_TEST.ready()');c('[data-tool=color]');c('#view3d');pg.wait_for_function('BEAUTY_TEST.render3d()>0');pg.locator('#model').scroll_into_view_if_needed()
 def point(kind,selector,hit='hit3d'):
  return pg.evaluate('''([k,sel,h])=>{let d=BEAUTY_TEST[h](),r=document.querySelector(sel).getBoundingClientRect(),s=Math.min(r.width/d.w,r.height/d.h);let i=d.kind.findIndex((x,i)=>x===k&&(h==='handsHit'||d.front[i]));if(i<0)return null;return [r.left+(r.width-d.w*s)/2+(i%d.w+.5)*s,r.top+(r.height-d.h*s)/2+(Math.floor(i/d.w)+.5)*s]}''',[kind,selector,hit])
 xy=point(2,'#model');assert xy;pg.touchscreen.tap(*xy);pg.wait_for_timeout(250);check('Tinte aplicado por toque directamente sobre malla 3D',ev('BEAUTY_TEST.look().strokes.length')>0);n=ev('BEAUTY_TEST.render3d()');c('#rotateRight');pg.wait_for_function(f'BEAUTY_TEST.render3d()>{n}');check('Giro 3D después de teñir',ev('BEAUTY_TEST.show3d()'));c('#chooseStyle');c('[data-style=hair-001]');pg.wait_for_timeout(400);check('Peinado sin abandonar vista 3D',ev('BEAUTY_TEST.show3d()&&BEAUTY_TEST.look().style==="hair-001"'));c('[data-mode=nails]');c('#view3d');pg.wait_for_function('BEAUTY_TEST.handsHit()!==null');pg.locator('#hands3d').scroll_into_view_if_needed();xy=point(13,'#hands3d','handsHit');assert xy;pg.touchscreen.tap(*xy);pg.wait_for_timeout(300);check('Esmalte aplicado directamente sobre mano 3D',ev('BEAUTY_TEST.look().nails[2].color!=="#f3b9b3"'));c('[data-tool=heart]');pg.locator('#hands3d').scroll_into_view_if_needed();xy=point(13,'#hands3d','handsHit');pg.touchscreen.tap(*xy);pg.wait_for_timeout(250);check('Decoración de uña en mano 3D',ev('BEAUTY_TEST.look().nails[2].art==="heart"'))
 for room in ['modern','victorian','shimokitazawa']:
  c('#roomChange');c('[data-room='+room+']');c('#roomChange');c('#roomInspect');pg.wait_for_timeout(1000);check('Vista 3D de '+room,pg.locator('#room3dDialog').is_visible() and ev('document.querySelector("#roomModel").getContext("2d").getImageData(0,0,450,350).data.some(x=>x>0)'));c('#room3dClose')
 check('Sin excepciones JS en emulación móvil táctil',not err);b.close()
Path('v7focused_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
