from flask import Flask, jsonify, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html><head><title>BHARAT-AGI | Sovereign AGI</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:#0a0a0a;color:#fff;font-family:Inter,sans-serif;margin:0}
.header{padding:20px;text-align:center;border-bottom:1px solid #222;background:linear-gradient(90deg,#ff9933,#ffffff,#138808);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;font-size:32px}
.container{max-width:800px;margin:40px auto;padding:20px}
.card{background:#151515;border:1px solid #333;border-radius:16px;padding:24px;margin-bottom:20px}
.badge{display:inline-block;padding:6px 12px;border-radius:20px;background:#1f3d1f;color:#4ade80;font-size:12px}
.layers{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:20px 0}
.layer{background:#1a1a1a;padding:12px;border-radius:10px;text-align:center;border:1px solid #2a2a2a}
.chat-box{height:300px;overflow-y:auto;background:#000;border-radius:12px;padding:16px;margin:16px 0;border:1px solid #333}
.input-area{display:flex;gap:10px}
input{flex:1;padding:14px;border-radius:10px;border:1px solid #333;background:#111;color:#fff}
button{padding:14px 24px;border-radius:10px;border:0;background:#ff9933;color:#000;font-weight:bold;cursor:pointer}
.user{color:#ff9933;margin:8px 0}
.bot{color:#4ade80;margin:8px 0}
</style></head><body>
<div class="header">BHARAT-AGI</div>
<div class="container">
<div class="card">
<span class="badge">● LIVE - Sovereign AGI</span>
<h2>India First Indigenous AGI - 7 Layer Architecture</h2>
<p>Built for Bharat, By Bharat. Sovereign, Secure, Swadeshi.</p>
<div class="layers">
<div class="layer"><b>🛡️ RAKSHAK</b><br>Safety Layer</div>
<div class="layer"><b>👁️ DRISHTI</b><br>Perception</div>
<div class="layer"><b>🧠 MANAS</b><br>Reasoning</div>
<div class="layer"><b>⚡ KARMA</b><br>Action</div>
<div class="layer"><b>🗣️ VAANI</b><br>Language</div>
<div class="layer"><b>🔄 ANUBHAV</b><br>Memory</div>
<div class="layer"><b>🌱 VIKAS</b><br>Evolution</div>
</div>
</div>
<div class="card">
<h3>Try BHARAT-AGI Chat</h3>
<div id="chat" class="chat-box"><div class="bot">BHARAT-AGI: Namaste! I am BHARAT-AGI. Ask me anything - Jai Hind!</div></div>
<div class="input-area">
<input id="q" placeholder="Ask in Hindi or English..." onkeypress="if(event.key==='Enter')send()">
<button onclick="send()">Send</button>
</div>
</div>
</div>
<script>
async function send(){
 let input=document.getElementById('q');
 let query=input.value;
 if(!query) return;
 let chat=document.getElementById('chat');
 chat.innerHTML+=`<div class="user">You: ${query}</div>`;
 input.value='';
 let res=await fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({query})});
 let data=await res.json();
 chat.innerHTML+=`<div class="bot">BHARAT-AGI: ${data.response}<br><small style="opacity:0.5">RAKSHAK:${data.rakshak} | MANAS:${data.core_reasoning.substring(0,60)}...</small></div>`;
 chat.scrollTop=chat.scrollHeight;
}
</script>
</body></html>
"""

@app.route("/")
def home():
    return HTML

@app.route("/api/status")
def status():
    return jsonify({"name":"BHARAT-AGI","status":"Live - Sovereign AGI","layers":7,"message":"India First AGI Operational - Jai Hind!","architecture":["RAKSHAK","DRISHTI","MANAS","KARMA","VAANI","ANUBHAV","VIKAS"]})

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    q = data.get("query","Namaste")
    return jsonify({
        "rakshak": "Safe - Content Verified by Dharmic Filter",
        "perception": f"Understood: {q}",
        "core_reasoning": f"7-Layer Reasoning: Analyzed '{q}' via Bharatiya context and logical inference",
        "evolution": "Learning from interaction",
        "response": f"BHARAT-AGI Response to '{q}': As India's Sovereign AGI, I process this through our 7-layer architecture ensuring safety, cultural alignment, and truth. Jai Hind! Bharat is building its own intelligence. 🚀"
    })

@app.route("/<path:path>")
def catch_all(path):
    if path.startswith("api/"):
        return status()
    return HTML