from pathlib import Path
from playwright.sync_api import sync_playwright
import re,json
P=Path('/mnt/data/Royal_Beauty_Studio_V9_autonomo.html'); results=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);pg=b.new_page(viewport={'width':1200,'height':780});pg.set_default_timeout(30000);err=[];pg.on('pageerror',lambda e:err.append(str(e)));pg.evaluate("Object.defineProperty(window,'localStorage',{value:{getItem(k){return this[k]??null},setItem(k,v){this[k]=v}}})");html=P.read_text();scripts=re.findall(r'<script>(.*?)</script>',html,re.S);pg.set_content(re.sub(r'<script>.*?</script>','',html,flags=re.S),wait_until='load',timeout=30000)
 for script in scripts:pg.add_script_tag(content=script)
 def c(sel):pg.locator(sel).first.click()
 def ev(s):return pg.evaluate(s)
 def check(name,val):
  assert val,name;results.append(name);print('PASS',name,flush=True)
 pg.wait_for_function('document.querySelector("#homeWorld").dataset.room');check('Cuatro modalidades',pg.locator('[data-home-mode]').count()==4);pg.screenshot(path='/mnt/data/Royal_Beauty_V9_home.png');check('Salón rosa por defecto',ev('BEAUTY_TEST.state.room==="pink"'));check('Cinco escenarios',pg.locator('button[data-room]').count()==5);pg.set_viewport_size({'width':390,'height':844});pg.wait_for_timeout(250);pg.screenshot(path='/mnt/data/Royal_Beauty_V9_movil.png',full_page=True);check('Portada móvil sin desbordamiento',ev('document.documentElement.scrollWidth<=innerWidth'));pg.set_viewport_size({'width':1200,'height':780});c('#musicOpen');check('Tres canciones originales',pg.locator('#musicTrack option').count()==3);pg.locator('#musicTrack').select_option('2');check('Canción guardada',ev('BEAUTY_TEST.state.musicTrack===2'));c('#musicClose');c('#customize');c('#customRoom');c('[data-room=palace]');pg.wait_for_function('document.querySelector("#homeWorld").dataset.room==="palace:true"');check('Torre 3D cargada',ev('TOWER_MESH.length>0'));c('#customize');c('#customRoom');c('[data-room=pink]');c('[data-home-mode=relax]');pg.screenshot(path='/mnt/data/Royal_Beauty_V9_selector.png');c('#characterConfirm');pg.wait_for_function('BEAUTY_TEST.hit3d()!==null && BEAUTY_TEST.worldReady()');check('Relajación comienza en peluquería 3D',ev('BEAUTY_TEST.state.relax&&BEAUTY_TEST.mode()==="hair"&&BEAUTY_TEST.show3d()'));pg.screenshot(path='/mnt/data/Royal_Beauty_V9_salon.png')
 def stroke(t,n):
  c('[data-tool='+t+']');pg.locator('#model').scroll_into_view_if_needed()
  for attempt in range(n+5):
   before=ev(f'BEAUTY_TEST.look().work.{t}||0')
   if before>=n:return
   pt=pg.evaluate('''t=>{let d=BEAUTY_TEST.hit3d(),r=document.querySelector('#model').getBoundingClientRect(),s=Math.min(r.width/d.w,r.height/d.h),seen=new Set(BEAUTY_TEST.look().visited?.[t]||[]);for(let i=0;i<d.kind.length;i+=11){let x=d.x[i],y=d.y[i];if(!d.kind[i]||!d.front[i]||!BEAUTY_TEST.validTarget(x,y,d.kind[i]===2))continue;let k=Math.floor(x/18)+':'+Math.floor(y/18);if(seen.has(k))continue;return [r.left+(r.width-d.w*s)/2+(i%d.w+.5)*s,r.top+(r.height-d.h*s)/2+(Math.floor(i/d.w)+.5)*s]}return null}''',t)
   assert pt,(t,before);pg.mouse.click(*pt);pg.wait_for_timeout(340)
  print(t,'count',ev(f'BEAUTY_TEST.look().work.{t}||0'),flush=True)
 for t in ['brush','color','shine']:stroke(t,4)
 check('Pelo progresa mediante interacción 3D',ev('BEAUTY_TEST.quality("hair")===1'));c('#finish');c('#continue');pg.wait_for_function('BEAUTY_TEST.ready()&&BEAUTY_TEST.show3d()');check('Relajación avanza a maquillaje',ev('BEAUTY_TEST.mode()==="makeup"&&BEAUTY_TEST.state.relaxDone.length===1'))
 for t in ['lip','shadow','blush']:stroke(t,3)
 check('Maquillaje 3D completo',ev('BEAUTY_TEST.quality("makeup")===1'));c('#finish');c('#continue');pg.wait_for_function('BEAUTY_TEST.handsHit()!==null');check('Manicura siempre 3D',ev('BEAUTY_TEST.show3d()&&BEAUTY_TEST.mode()==="nails"'));pg.locator('#hands3d').scroll_into_view_if_needed()
 for i in range(10):
  xy=pg.evaluate('''k=>{let d=BEAUTY_TEST.handsHit(),r=document.querySelector('#hands3d').getBoundingClientRect(),s=Math.min(r.width/d.w,r.height/d.h);let i=d.kind.findIndex(x=>x===k);return [r.left+(r.width-d.w*s)/2+(i%d.w+.5)*s,r.top+(r.height-d.h*s)/2+(Math.floor(i/d.w)+.5)*s]}''',11+i);pg.mouse.click(*xy);pg.wait_for_timeout(100)
 check('Diez uñas tratadas en 3D',ev('BEAUTY_TEST.quality("nails")===1'));c('#finish');c('#continue');check('Día completo, nueve estrellas',ev('BEAUTY_TEST.state.stars===9&&!BEAUTY_TEST.state.relax'));check('Sin errores JS',not err);b.close()
Path('/mnt/data/Royal_Beauty_V9_pruebas.txt').write_text('\n'.join(results))
