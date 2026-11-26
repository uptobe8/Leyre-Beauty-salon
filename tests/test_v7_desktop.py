from pathlib import Path
from playwright.sync_api import sync_playwright
import json
import sys
P=Path(sys.argv[1] if len(sys.argv)>1 else 'Royal_Beauty_Studio_V7_revision_autonomo.html'); results=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);pg=b.new_page(viewport={'width':1050,'height':800});pg.set_default_timeout(10000);err=[];pg.on('pageerror',lambda e:err.append(str(e)));pg.on('dialog',lambda d:d.accept());pg.evaluate("Object.defineProperty(window,'localStorage',{value:{getItem(k){return this[k]??null},setItem(k,v){this[k]=v}}})");html=P.read_text();import re; scripts=re.findall(r'<script>(.*?)</script>',html,re.S);pg.set_content(re.sub(r'<script>.*?</script>','',html,flags=re.S),wait_until='load',timeout=30000);print('DOM loaded',flush=True)
 for i,script in enumerate(scripts):
  print('loading script',i,len(script),flush=True);pg.add_script_tag(content=script)

 def c(s):pg.locator(s).first.click()
 def ev(s):return pg.evaluate(s)
 def check(name,val):
  assert val,name;results.append(name);print('PASS',name,flush=True)
 def ready():pg.wait_for_function('BEAUTY_TEST.ready()')
 def select(id):c('#changePerson');c('[data-person='+id+']');c('#characterConfirm');ready()
 def stroke(tool,n=5):
  c('[data-tool='+tool+']');pg.locator('#portrait').scroll_into_view_if_needed();pts=ev('''n=>{let r=document.querySelector('#portrait').getBoundingClientRect(),s=Math.min(r.width/480,r.height/576),a=[],cells=new Set();for(let y=12;y<570;y+=5)for(let x=12;x<475;x+=5){if(!BEAUTY_TEST.validTarget(x,y))continue;let k=Math.floor(x/18)+':'+Math.floor(y/18);if(cells.has(k))continue;cells.add(k);a.push([r.left+(r.width-480*s)/2+x*s,r.top+(r.height-576*s)/2+y*s]);if(a.length>=n)return a}return a}''',n) if False else pg.evaluate('''n=>{let r=document.querySelector('#portrait').getBoundingClientRect(),s=Math.min(r.width/480,r.height/576),a=[],cells=new Set();for(let y=12;y<570;y+=5)for(let x=12;x<475;x+=5){if(!BEAUTY_TEST.validTarget(x,y))continue;let k=Math.floor(x/18)+':'+Math.floor(y/18);if(cells.has(k))continue;cells.add(k);a.push([r.left+(r.width-480*s)/2+x*s,r.top+(r.height-576*s)/2+y*s]);if(a.length>=n)return a}return a}''',n)
  assert len(pts)>=n,(tool,len(pts));pg.mouse.move(*pts[0]);pg.mouse.down();
  for x,y in pts[1:]:pg.mouse.move(x,y);pg.wait_for_timeout(20)
  pg.mouse.up();pg.wait_for_timeout(100)
 check('Continuar desactivado en partida nueva',pg.locator('#homeContinue').is_disabled());c('[data-home-mode=hair]');c('[data-person=elsa]');c('#selectorBack');check('Cancelar selector no cambia personaje',ev('BEAUTY_TEST.state.person')=='rapunzel');c('[data-home-mode=hair]');c('#characterConfirm');ready();check('un toque no completa servicio',pg.locator('#finish').is_disabled());c('[data-tool=color]');pg.locator('#portrait').dispatch_event('pointerdown',{'clientX':0,'clientY':0,'pointerId':1});pg.locator('#portrait').dispatch_event('pointerup',{'pointerId':1});check('fuera del cabello no aplica tinte',ev('BEAUTY_TEST.look().strokes.length')==0)
 for t in ['wash','rinse','dryer','brush','color','scissors','shine','flower']:
  stroke(t,7 if t in ['wash','rinse','dryer'] else 4);check('herramienta '+t,ev(f'(BEAUTY_TEST.look().work.{t}||0)>0'))
 check('tijeras recortan',ev('BEAUTY_TEST.look().trim>0'));check('tinte por trazos',ev('BEAUTY_TEST.look().strokes.length>0'));check('progreso pelo',ev('BEAUTY_TEST.quality("hair")')==1)
 c('#finish');check('3 estrellas',ev('BEAUTY_TEST.state.stars')==3);c('#continue');check('avanza a maquillaje',ev('BEAUTY_TEST.mode()')=='makeup');ready();check('maquillaje empieza sin progreso',pg.locator('#finish').is_disabled());
 for t in ['lip','shadow','blush','glitter']:
  stroke(t,3);check('maquillaje local '+t,ev(f'BEAUTY_TEST.look().makeupStrokes.{t}.length>0'))
 check('maquillaje progresivo',ev('BEAUTY_TEST.quality("makeup")')==1);c('#finish');c('#continue');check('10 uñas',pg.locator('.nail').count()==10)
 c('[data-tool=heart]');c('[data-nail="2"]');c('[data-tool=polish]');c('[data-nail="2"]');check('esmalte conserva decoración',ev('BEAUTY_TEST.look().nails[2].art')=='heart');c('[data-tool=file]');c('[data-nail="2"]');check('limado',ev('BEAUTY_TEST.look().nails[2].filed')==1);c('[data-tool=remove]');c('[data-nail="2"]');check('retirada esmalte',ev('BEAUTY_TEST.look().nails[2].art===""&&BEAUTY_TEST.look().nails[2].color==="#f3b9b3"'));c('[data-tool=polish]');
 for i in range(10):c(f'[data-nail="{i}"]')
 check('manicura requiere diez uñas',ev('BEAUTY_TEST.quality("nails")')==1);c('#view3d');pg.wait_for_function('BEAUTY_TEST.handsHit()!==null');check('manos 3D con diez regiones',ev('new Set(BEAUTY_TEST.handsHit().kind.filter(x=>x>=11)).size')==10);pg.screenshot(path='V7_manos_3D.png',full_page=True);c('#rotateRight');c('#view3d');c('#finish');c('#continue');check('9 estrellas por tres servicios',ev('BEAUTY_TEST.state.stars')==9);c('#homeContinue');c('[data-mode=hair]');c('#reset');check('reinicio conserva historial de premios y borra progreso',ev('BEAUTY_TEST.state.stars===9&&BEAUTY_TEST.quality("hair")===0'));ready();
 for t in ['brush','color','shine']:stroke(t,5)
 c('#finish');check('no duplica premios tras reiniciar',ev('BEAUTY_TEST.state.stars')==9);c('#continue');c('[data-mode=hair]');c('#undo');check('deshacer no concede estrellas',ev('BEAUTY_TEST.state.stars')==9);
 for id in ['rapunzel','anna','elsa','snow-white']:
  select(id);c('#chooseStyle');check(id+' 16 opciones',pg.locator('.styleChoice').count()==16);c('[data-style=hair-curly]');ready();c('#view3d');pg.wait_for_function('BEAUTY_TEST.hit3d()!==null');pg.wait_for_timeout(300);check(id+' 3D con peinado',ev('BEAUTY_TEST.show3d()&&BEAUTY_TEST.look().style==="hair-curly"'));c('#view3d')
 c('#roomChange');c('[data-room=modern]');c('#roomChange');c('#roomInspect');pg.wait_for_function('document.querySelector("#roomModel").width===450');c('#roomRight');pg.wait_for_timeout(500);check('salón 3D giratorio',pg.locator('#room3dDialog').is_visible());pg.screenshot(path='V7_salon_3D.png',full_page=True);c('#room3dClose');check('guardado local',ev('JSON.parse(localStorage.getItem("royal_beauty_v1")).stars===9'));check('sin excepciones JavaScript',not err);b.close()
Path('v7results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
