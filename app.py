HTML = '''<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Book a Lesson — Club 72 Golf Co.</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #f5f0e8; min-height: 100vh; padding: 2rem 1rem; }
.wrap { max-width: 640px; margin: 0 auto; background: #fff; border-radius: 12px; padding: 2rem; box-shadow: 0 2px 24px rgba(26,58,42,0.10); }
.brand { display: flex; align-items: center; gap: 10px; margin-bottom: 1.5rem; padding-bottom: 1.25rem; border-bottom: 1px solid #e8e0cc; }
.brand-dot { width: 36px; height: 36px; border-radius: 50%; background: #1a3a2a; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 13px; color: #b8963e; flex-shrink: 0; }
.brand-name { font-size: 16px; font-weight: 600; color: #1a3a2a; }
.brand-sub { font-size: 13px; color: #7a7a6e; }
.step-bar { display: flex; margin-bottom: 2rem; }
.step { flex: 1; display: flex; align-items: center; gap: 8px; }
.step-num { width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 600; flex-shrink: 0; background: #f0ead8; color: #7a7a6e; border: 1px solid #d4cdb8; }
.step-num.active { background: #1a3a2a; color: #b8963e; border-color: #1a3a2a; }
.step-num.done { background: #e8f4ec; color: #2d5a3d; border-color: #c8dece; }
.step-lbl { font-size: 12px; color: #7a7a6e; }
.step-lbl.active { color: #1a3a2a; font-weight: 600; }
.step-line { flex: 1; height: 1px; background: #e8e0cc; margin: 0 6px; }
.panel { display: none; }
.panel.active { display: block; }
h2 { font-size: 20px; font-weight: 600; color: #1a3a2a; margin-bottom: 4px; }
.sub { font-size: 14px; color: #7a7a6e; margin-bottom: 1.5rem; }
.pkg-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 10px; margin-bottom: 1.5rem; }
@media(max-width:480px){.pkg-grid{grid-template-columns:1fr;}}
.pkg-card { border: 1px solid #d4cdb8; border-radius: 10px; padding: 14px; cursor: pointer; transition: all 0.15s; }
.pkg-card:hover { border-color: #1a3a2a; }
.pkg-card.sel { border: 2px solid #1a3a2a; background: #f5f0e8; }
.pkg-badge { font-size: 11px; font-weight: 600; color: #2d5a3d; background: #e8f4ec; padding: 2px 8px; border-radius: 20px; display: inline-block; margin-bottom: 8px; }
.pkg-badge.gold { background: #fdf3de; color: #7a5a1a; }
.pkg-name { font-size: 14px; font-weight: 600; color: #1a1a1a; margin-bottom: 3px; }
.pkg-price { font-size: 22px; font-weight: 700; color: #1a3a2a; margin-bottom: 6px; }
.pkg-price span { font-size: 12px; font-weight: 400; color: #7a7a6e; }
.pkg-desc { font-size: 12px; color: #7a7a6e; line-height: 1.5; }
.cal-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem; }
.cal-month { font-size: 15px; font-weight: 600; color: #1a3a2a; }
.cal-nav { background: none; border: 1px solid #d4cdb8; border-radius: 6px; padding: 4px 12px; cursor: pointer; font-size: 16px; color: #3d3d3d; }
.cal-nav:hover { background: #f5f0e8; }
.cal-grid { display: grid; grid-template-columns: repeat(7,1fr); gap: 4px; margin-bottom: 1rem; }
.cal-dlbl { text-align: center; font-size: 12px; color: #7a7a6e; padding: 4px 0; font-weight: 500; }
.cal-day { text-align: center; padding: 9px 4px; font-size: 14px; border-radius: 6px; cursor: pointer; color: #1a1a1a; }
.cal-day:hover:not(.empty):not(.past):not(.na) { background: #f0ead8; }
.cal-day.empty,.cal-day.past,.cal-day.na { cursor: default; color: #c8c2b0; }
.cal-day.na { text-decoration: line-through; }
.cal-day.sel { background: #1a3a2a; color: #b8963e; font-weight: 700; border-radius: 50%; }
.cal-day.today { font-weight: 700; color: #1a3a2a; }
.time-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 8px; margin-bottom: 1.5rem; }
@media(max-width:480px){.time-grid{grid-template-columns:repeat(3,1fr);}}
.ts { border: 1px solid #d4cdb8; border-radius: 8px; padding: 10px 6px; text-align: center; cursor: pointer; font-size: 13px; }
.ts:hover:not(.tk) { border-color: #1a3a2a; background: #f5f0e8; }
.ts.sel { border: 2px solid #1a3a2a; background: #f5f0e8; color: #1a3a2a; font-weight: 600; }
.ts.tk { color: #c8c2b0; cursor: default; text-decoration: line-through; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px; }
@media(max-width:480px){.form-row{grid-template-columns:1fr;}}
.form-row.full { grid-template-columns: 1fr; }
.fg { display: flex; flex-direction: column; gap: 5px; }
label { font-size: 13px; color: #7a7a6e; font-weight: 500; }
input,select,textarea { width: 100%; padding: 9px 12px; border: 1px solid #d4cdb8; border-radius: 8px; font-size: 14px; font-family: inherit; color: #1a1a1a; outline: none; }
input:focus,select:focus,textarea:focus { border-color: #1a3a2a; box-shadow: 0 0 0 3px rgba(26,58,42,0.08); }
textarea { height: 80px; resize: vertical; }
.ck-row { display: flex; align-items: center; gap: 8px; margin-bottom: 1rem; }
.ck-row input { width: auto; }
.ck-row label { font-size: 13px; color: #3d3d3d; margin: 0; }
.sum { background: #f8f3e8; border-radius: 10px; padding: 1rem 1.25rem; margin-bottom: 1.5rem; border: 1px solid #e8e0cc; }
.sr { display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid #e8e0cc; font-size: 13px; }
.sr:last-child { border-bottom: none; font-weight: 700; font-size: 15px; }
.sr span:first-child { color: #7a7a6e; }
.sr span:last-child { color: #1a1a1a; }
.btn-row { display: flex; gap: 10px; }
.btn { padding: 11px 22px; border-radius: 8px; font-size: 14px; cursor: pointer; font-family: inherit; font-weight: 600; transition: all 0.15s; }
.btn-p { background: #1a3a2a; color: #b8963e; border: none; flex: 1; }
.btn-p:hover { background: #2d5a3d; }
.btn-p:disabled { background: #e8e0cc; color: #7a7a6e; cursor: not-allowed; }
.btn-s { background: none; border: 1px solid #d4cdb8; color: #7a7a6e; }
.btn-s:hover { background: #f5f0e8; }
.err { font-size: 12px; color: #a32d2d; margin-top: 10px; display: none; }
.ok-wrap { text-align: center; padding: 2rem 0; }
.ok-icon { width: 60px; height: 60px; border-radius: 50%; background: #e8f4ec; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 26px; }
.ok-title { font-size: 22px; font-weight: 700; color: #1a3a2a; margin-bottom: 8px; }
.ok-sub { font-size: 14px; color: #7a7a6e; margin-bottom: 1.5rem; line-height: 1.6; }
.conf { background: #f8f3e8; border-radius: 10px; padding: 1rem 1.25rem; text-align: left; max-width: 380px; margin: 0 auto 1.5rem; border: 1px solid #e8e0cc; }
.cr { display: flex; justify-content: space-between; padding: 5px 0; border-bottom: 1px solid #e8e0cc; font-size: 13px; }
.cr:last-child { border-bottom: none; }
.cr span:first-child { color: #7a7a6e; }
.cr span:last-child { color: #1a1a1a; font-weight: 600; }
.contact-note { font-size: 13px; color: #7a7a6e; }
.contact-note strong { color: #1a3a2a; }
</style></head><body>
<div class="wrap">
  <div class="brand">
    <div class="brand-dot">72</div>
    <div>
      <div class="brand-name">Club 72 Golf Co.</div>
      <div class="brand-sub">Book a lesson with Nathan Ross</div>
    </div>
  </div>
  <div class="step-bar" id="sb">
    <div class="step"><div class="step-num active" id="sn1">1</div><div class="step-lbl active" id="sl1">Package</div></div>
    <div class="step-line"></div>
    <div class="step"><div class="step-num" id="sn2">2</div><div class="step-lbl" id="sl2">Date & time</div></div>
    <div class="step-line"></div>
    <div class="step"><div class="step-num" id="sn3">3</div><div class="step-lbl" id="sl3">Details</div></div>
    <div class="step-line"></div>
    <div class="step"><div class="step-num" id="sn4">4</div><div class="step-lbl" id="sl4">Confirm</div></div>
  </div>

  <div class="panel active" id="p1">
    <h2>Choose a package</h2>
    <p class="sub">All lessons at Club 72, Berwick ME or a local course of your choice.</p>
    <div class="pkg-grid">
      <div class="pkg-card" data-pkg="Introductory · 60 min" data-price="90" onclick="selPkg(this)">
        <span class="pkg-badge">Single</span>
        <div class="pkg-name">Introductory</div>
        <div class="pkg-price">$90 <span>/ session</span></div>
        <div class="pkg-desc">Full swing evaluation with TrackMan analysis.</div>
      </div>
      <div class="pkg-card" data-pkg="Series of Five" data-price="400" onclick="selPkg(this)">
        <span class="pkg-badge gold">Most popular</span>
        <div class="pkg-name">Series of Five</div>
        <div class="pkg-price">$400 <span>/ 5 lessons</span></div>
        <div class="pkg-desc">Committed improvement. Save $50 vs individual.</div>
      </div>
      <div class="pkg-card" data-pkg="Monthly Retainer" data-price="320" onclick="selPkg(this)">
        <span class="pkg-badge">Elite</span>
        <div class="pkg-name">Monthly Retainer</div>
        <div class="pkg-price">$320 <span>/ month</span></div>
        <div class="pkg-desc">4 lessons/month with on-course playing lesson.</div>
      </div>
    </div>
    <div class="form-row full" style="margin-bottom:1rem;">
      <div class="fg"><label>Location preference</label>
        <select id="loc"><option>Club 72 — 12 Sullivan St, Berwick ME</option><option>Local course of my choice</option></select>
      </div>
    </div>
    <div class="btn-row"><button class="btn btn-p" id="btn1" onclick="go(2)" disabled>Continue to date &amp; time</button></div>
  </div>

  <div class="panel" id="p2">
    <h2>Pick a date and time</h2>
    <p class="sub">Mon–Fri 9am–6pm · Sat 11am–5pm · Sun by request</p>
    <div class="cal-header">
      <button class="cal-nav" onclick="prevM()">&#8249;</button>
      <span class="cal-month" id="cMonth"></span>
      <button class="cal-nav" onclick="nextM()">&#8250;</button>
    </div>
    <div class="cal-grid" id="cGrid"></div>
    <div id="tSec" style="display:none;">
      <p style="font-size:13px;color:#7a7a6e;margin-bottom:10px;font-weight:500;" id="tLabel"></p>
      <div class="time-grid" id="tGrid"></div>
    </div>
    <p class="err" id="e2">Please select a date and time.</p>
    <div class="btn-row">
      <button class="btn btn-s" onclick="go(1)">Back</button>
      <button class="btn btn-p" id="btn2" onclick="v2()" disabled>Continue to details</button>
    </div>
  </div>

  <div class="panel" id="p3">
    <h2>Your details</h2>
    <p class="sub">So Nathan can reach you to confirm your lesson.</p>
    <div class="form-row">
      <div class="fg"><label>First name *</label><input id="fn" placeholder="Jane" oninput="ck3()"></div>
      <div class="fg"><label>Last name *</label><input id="ln" placeholder="Smith" oninput="ck3()"></div>
    </div>
    <div class="form-row">
      <div class="fg"><label>Email *</label><input type="email" id="em" placeholder="jane@example.com" oninput="ck3()"></div>
      <div class="fg"><label>Phone *</label><input type="tel" id="ph" placeholder="207-555-0100" oninput="ck3()"></div>
    </div>
    <div class="form-row full">
      <div class="fg"><label>Skill level</label>
        <select id="sk">
          <option>Complete beginner</option><option>Casual player (100+ shots)</option>
          <option>Intermediate (80–100)</option><option>Experienced (below 80)</option>
          <option>Competitive / tournament player</option>
        </select>
      </div>
    </div>
    <div class="form-row full">
      <div class="fg"><label>Anything Nathan should know? (optional)</label>
        <textarea id="nt" placeholder="E.g. working on my short game, have a bad back..."></textarea>
      </div>
    </div>
    <div class="ck-row"><input type="checkbox" id="tos" onchange="ck3()">
      <label for="tos">I understand Nathan has a 24-hour cancellation policy.</label>
    </div>
    <p class="err" id="e3">Please fill in all required fields and accept the cancellation policy.</p>
    <div class="btn-row">
      <button class="btn btn-s" onclick="go(2)">Back</button>
      <button class="btn btn-p" id="btn3" onclick="v3()" disabled>Review &amp; confirm</button>
    </div>
  </div>

  <div class="panel" id="p4">
    <h2>Review your booking</h2>
    <p class="sub">Confirm the details below. Nathan will reach out within 24 hours.</p>
    <div class="sum" id="sumCard"></div>
    <div class="btn-row">
      <button class="btn btn-s" onclick="go(3)">Back</button>
      <button class="btn btn-p" onclick="submit()">Confirm booking</button>
    </div>
  </div>

  <div class="panel" id="p5">
    <div class="ok-wrap">
      <div class="ok-icon">&#10003;</div>
      <div class="ok-title">Booking request sent!</div>
      <p class="ok-sub">Nathan will reach out to <strong id="confEm"></strong> within 24 hours to confirm. See you on the course!</p>
      <div class="conf" id="confCard"></div>
      <p class="contact-note">Questions? Call or text <strong>207-289-4970</strong> · <strong>Nate@club72golfco.com</strong></p>
    </div>
  </div>
</div>
<script>
const MONTHS=["January","February","March","April","May","June","July","August","September","October","November","December"];
const DAYS=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];
let S={pkg:null,price:null,date:null,dateLabel:null,time:null};
let cY,cM;
(function(){const n=new Date();cY=n.getFullYear();cM=n.getMonth();rCal();}());
function selPkg(el){document.querySelectorAll('.pkg-card').forEach(c=>c.classList.remove('sel'));el.classList.add('sel');S.pkg=el.dataset.pkg;S.price=el.dataset.price;document.getElementById('btn1').disabled=false;}
function go(n){document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));document.getElementById('p'+n).classList.add('active');updBar(n);}
function updBar(n){for(let i=1;i<=4;i++){const num=document.getElementById('sn'+i),lbl=document.getElementById('sl'+i);if(i<n){num.className='step-num done';num.textContent='✓';lbl.className='step-lbl';}else if(i===n){num.className='step-num active';num.textContent=i;lbl.className='step-lbl active';}else{num.className='step-num';num.textContent=i;lbl.className='step-lbl';}}}
function prevM(){cM--;if(cM<0){cM=11;cY--;}rCal();}
function nextM(){cM++;if(cM>11){cM=0;cY++;}rCal();}
function rCal(){document.getElementById('cMonth').textContent=MONTHS[cM]+' '+cY;const g=document.getElementById('cGrid');g.innerHTML='';DAYS.forEach(d=>{const e=document.createElement('div');e.className='cal-dlbl';e.textContent=d;g.appendChild(e);});const f=new Date(cY,cM,1).getDay(),days=new Date(cY,cM+1,0).getDate(),today=new Date();today.setHours(0,0,0,0);for(let i=0;i<f;i++){const e=document.createElement('div');e.className='cal-day empty';g.appendChild(e);}for(let d=1;d<=days;d++){const e=document.createElement('div');e.className='cal-day';e.textContent=d;const date=new Date(cY,cM,d);date.setHours(0,0,0,0);const dow=date.getDay();if(date<today){e.classList.add('past');}else if(dow===0){e.classList.add('na');}else{if(date.toDateString()===today.toDateString())e.classList.add('today');const key=cY+'-'+(cM+1)+'-'+d;if(S.date===key)e.classList.add('sel');e.addEventListener('click',()=>selDate(d,date,dow));}g.appendChild(e);}}
function selDate(d,date,dow){S.date=cY+'-'+(cM+1)+'-'+d;S.dateLabel=MONTHS[cM]+' '+d+', '+cY;S.time=null;document.getElementById('btn2').disabled=true;rCal();rTimes(dow);document.getElementById('tSec').style.display='block';document.getElementById('tLabel').textContent='Available times — '+S.dateLabel;}
function rTimes(dow){const g=document.getElementById('tGrid');g.innerHTML='';const slots=dow===6?['11:00 am','12:00 pm','1:00 pm','2:00 pm','3:00 pm','4:00 pm']:['9:00 am','10:00 am','11:00 am','12:00 pm','1:00 pm','2:00 pm','3:00 pm','4:00 pm','5:00 pm'];const taken=[slots[1],slots[3]];slots.forEach(s=>{const e=document.createElement('div');e.className='ts';e.textContent=s;if(taken.includes(s)){e.classList.add('tk');}else{e.addEventListener('click',()=>{document.querySelectorAll('.ts').forEach(x=>x.classList.remove('sel'));e.classList.add('sel');S.time=s;document.getElementById('btn2').disabled=false;});}g.appendChild(e);});}
function v2(){if(!S.date||!S.time){document.getElementById('e2').style.display='block';return;}document.getElementById('e2').style.display='none';go(3);}
function ck3(){const ok=document.getElementById('fn').value.trim()&&document.getElementById('ln').value.trim()&&document.getElementById('em').value.trim()&&document.getElementById('ph').value.trim()&&document.getElementById('tos').checked;document.getElementById('btn3').disabled=!ok;}
function v3(){if(!document.getElementById('fn').value.trim()||!document.getElementById('ln').value.trim()||!document.getElementById('em').value.trim()||!document.getElementById('ph').value.trim()||!document.getElementById('tos').checked){document.getElementById('e3').style.display='block';return;}document.getElementById('e3').style.display='none';bldSum();go(4);}
function bldSum(){const loc=document.getElementById('loc').value,name=document.getElementById('fn').value+' '+document.getElementById('ln').value,em=document.getElementById('em').value,ph=document.getElementById('ph').value,sk=document.getElementById('sk').value;document.getElementById('sumCard').innerHTML=`<div class="sr"><span>Package</span><span>${S.pkg}</span></div><div class="sr"><span>Date</span><span>${S.dateLabel}</span></div><div class="sr"><span>Time</span><span>${S.time}</span></div><div class="sr"><span>Location</span><span>${loc}</span></div><div class="sr"><span>Name</span><span>${name}</span></div><div class="sr"><span>Email</span><span>${em}</span></div><div class="sr"><span>Phone</span><span>${ph}</span></div><div class="sr"><span>Skill level</span><span>${sk}</span></div><div class="sr"><span>Total due</span><span>$${S.price}</span></div>`;}
async function submit(){const data={name:document.getElementById('fn').value+' '+document.getElementById('ln').value,email:document.getElementById('em').value,phone:document.getElementById('ph').value,package:S.pkg,price:S.price,date:S.dateLabel,time:S.time,location:document.getElementById('loc').value,skill:document.getElementById('sk').value,notes:document.getElementById('nt').value};try{const r=await fetch('/book',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});const j=await r.json();if(j.ok){document.getElementById('confEm').textContent=data.email;document.getElementById('confCard').innerHTML=`<div class="cr"><span>Name</span><span>${data.name}</span></div><div class="cr"><span>Package</span><span>${data.package}</span></div><div class="cr"><span>Date & time</span><span>${data.date} at ${data.time}</span></div><div class="cr"><span>Location</span><span>${data.location}</span></div><div class="cr"><span>Total</span><span>$${data.price}</span></div>`;document.getElementById('sb').style.display='none';go(5);}else{alert('Something went wrong. Please try again.');}}catch(err){go(5);document.getElementById('confEm').textContent=data.email;document.getElementById('confCard').innerHTML=`<div class="cr"><span>Name</span><span>${data.name}</span></div><div class="cr"><span>Package</span><span>${data.package}</span></div><div class="cr"><span>Date & time</span><span>${data.date} at ${data.time}</span></div><div class="cr"><span>Total</span><span>$${data.price}</span></div>`;document.getElementById('sb').style.display='none';}}
</script></body></html>'''

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/book', methods=['POST'])
def book():
    d = request.get_json()
    conn = sqlite3.connect(DB)
    conn.execute('''INSERT INTO bookings (name,email,phone,package,price,date,time,location,skill,notes,created_at)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
        (d.get('name'), d.get('email'), d.get('phone'), d.get('package'),
         d.get('price'), d.get('date'), d.get('time'), d.get('location'),
         d.get('skill'), d.get('notes'), datetime.datetime.now().isoformat()))
    conn.commit()
    bids = conn.execute('SELECT last_insert_rowid()').fetchone()[0]
    conn.close()
    print(f"\n📅 NEW BOOKING #{bids}")
    print(f"   Name: {d.get('name')} | {d.get('email')} | {d.get('phone')}")
    print(f"   Package: {d.get('package')} (${d.get('price')})")
    print(f"   Date: {d.get('date')} at {d.get('time')}")
    print(f"   Location: {d.get('location')}")
    return jsonify({"ok": True, "id": bids})

@app.route('/bookings')
def bookings():
    conn = sqlite3.connect(DB)
    rows = conn.execute('SELECT * FROM bookings ORDER BY created_at DESC').fetchall()
    conn.close()
    out = "<h2 style='font-family:sans-serif;padding:1rem'>Bookings</h2><table border=1 cellpadding=8 style='font-family:sans-serif;font-size:13px;border-collapse:collapse'><tr><th>#</th><th>Name</th><th>Email</th><th>Phone</th><th>Package</th><th>Price</th><th>Date</th><th>Time</th><th>Location</th><th>Skill</th><th>Notes</th><th>Created</th></tr>"
    for r in rows:
        out += f"<tr>{''.join(f'<td>{x or ''}</td>' for x in r)}</tr>"
    out += "</table>"
    return out

if __name__ == '__main__':
    print("Starting Club 72 Booking Server on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
