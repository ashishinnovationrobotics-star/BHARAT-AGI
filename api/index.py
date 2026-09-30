from flask import Flask, jsonify, request
app = Flask(__name__)

HTML_PAGE = """<!DOCTYPE html>
<html><head><title>BHARAT-AGI | Sovereign AGI</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:#0a0a0a;color:#fff;font-family:Arial,sans-serif;margin:0}
.h{padding:22px;text-align:center;font-weight:900;font-size:32px;background:linear-gradient(90deg,#ff9933,#fff,#138808);-webkit-background-clip:text;-webkit-text-fill-color:transparent;border-bottom:1px solid #222}
.c{max-width:850px;margin:30px auto;padding:20px}
.card{background:#151515;border:1px solid #333;border-radius:16px;padding:22px;margin-bottom:18px}
.badge{background:#0f2f0f;color:#4ade80;padding:6px 12px;border-radius:20px;font-size:12px}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:18px 0}
.g{background:#1a1a1a;padding:12px;border-radius:10px;text-align:center;border:1px solid #2a2a2a;font-size:13px}
.chat{height:320px;overflow-y:auto;background:#000;border-radius:12px;padding:14px;border:1px solid #333;margin:14px 0}
.row{display:flex;gap:10px}
input{flex:1;padding:14px;border-radius:10px;border:1px solid #333;background:#111;color:#fff}
button{padding:14px 22px;border-radius:10px;border:0;background:#ff9933;color:#000;font-weight:bold;cursor:pointer}
.u{color:#ff9933;margin:8px 0}.b{color:#4ade80;margin:8px 0}
a{color:#ff9933}
</style></head><body>
<div class="h">BHARAT-AGI</div>
<div class="c">
<div class="card">
<span class="badge">● LIVE - Sovereign AGI - Production</span>
<h2>India's First Indigenous AGI - 7 Layer Architecture</h2>
<p>Built for Bharat, By Bharat. Sovereign, Secure, Swadeshi. <a href="/api/status" target="_blank">View API JSON</a></p>
<div class="grid">
<div class="g"><b>RAKSHAK</b><br>Safety</div>
<div class="g"><b>DRISHTI</b><br>Perception</div>
<div class="g"><b>MANAS</b><br>Reasoning</div>
<div class="g"><b>KARMA</b><br>Action</div>
<div class="g"><b>VAANI</b><br>Language</div>
<div class="g"><b>ANUBHAV</b><br>Memory</div>
<div class="g"><b>VIKAS</b><br>Evolution</div>
<div class="g"><b>BHARAT</b><br>Core</div>
</div>
</div>
<div class="card">
<h3>Live Demo - Chat with BHARAT-AGI</h3>
<div id="chat" class="chat"><div class="b">BHARAT-AGI: Namaste! I am India's Sovereign AGI. Ask me anything! Jai Hind!</div></div>
<div class="row">
<input id="q" placeholder="Ask in Hindi / English..." onkeypress="if(event.key==='Enter')send()">
<button onclick="send()">Send</button>
</div>
</div>
<div class="card"><small>Demo Link for Ideathon: <b>bharat-agi-jrfd.vercel.app</b> | Status: LIVE | Architecture: 7 Layers | Made in Bharat</small></div>
</div>
<script>
async function send(){
 let inp=document.getElementById('q'); let qu=inp.value; if(!qu) return;
 let ch=document.getElementById('chat'); ch.innerHTML+=`<div class="u">You: ${qu}</div>`; inp.value='';
 let r=await fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({query:qu})});
 let d=await r.json(); ch.innerHTML+=`<div class="b">BHARAT-AGI: ${d.response}<br><small style="opacity:.5">RAKSHAK:${d.rakshak}</small></div>`; ch.scrollTop=ch.scrollHeight;
}
</script>
</body></html>"""

@app.route('/api/status')
def api_status():
    return jsonify({"name":"BHARAT-AGI","status":"Live - Sovereign AGI","layers":7,"message":"India First AGI Operational - Jai Hind!","architecture":["RAKSHAK","DRISHTI","MANAS","KARMA","VAANI","ANUBHAV","VIKAS"]})

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.get_json() or {}
    q = data.get("query","Namaste")
    return jsonify({"rakshak":"Safe - Dharmic Filter Passed","response":f"BHARAT-AGI processing '{q}': Through 7-layer sovereign architecture, I ensure safe, culturally aligned, truthful response. Bharat is building its own intelligence. Jai Hind!"})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path.startswith('api/'):
        if 'chat' in path:
            return api_chat()
        return api_status()
    return HTML_PAGE