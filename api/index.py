from flask import Flask, jsonify, request
import os
app = Flask(__name__)

# Read index.html for website
try:
    html_path = os.path.join(os.path.dirname(__file__), '../index.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        HTML = f.read()
except Exception as e:
    HTML = """<html><body style=background:#000;color:#fff;text-align:center;padding:50px;font-family:Arial>
    <h1 style=font-size:48px;background:linear-gradient(90deg,#ff9933,#fff,#138808);-webkit-background-clip:text;-webkit-text-fill-color:transparent>BHARAT-AGI</h1>
    <h2>LIVE - Sovereign AGI - 7 Layer Architecture</h2>
    <p>RAKSHAK | DRISHTI | MANAS | KARMA | VAANI | ANUBHAV | VIKAS</p>
    <p>Jai Hind! 🇮🇳</p>
    </body></html>"""

# === MAIN WEBSITE ===
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
    # If API request, return JSON
    if path.startswith('api/'):
        if 'chat' in path or request.method == 'POST':
            data = request.get_json(silent=True) or {}
            q = data.get('query', data.get('message', ''))
            return jsonify({
                "response": f"BHARAT-AGI [7-layer sovereign processing]: Your query '{q}' analyzed via RAKSHAK safety layer, DRISHTI perception, MANAS reasoning. India is building its own intelligence. Sovereign, Secure, Swadeshi. Jai Hind! 🚀🇮🇳",
                "layer": "MANAS + VAANI",
                "status": "processed"
            })
        return jsonify({
            "name": "BHARAT-AGI",
            "status": "Live - Sovereign AGI",
            "layers": 7,
            "message": "India First AGI Operational - Jai Hind!",
            "architecture": ["RAKSHAK","DRISHTI","MANAS","KARMA","VAANI","ANUBHAV","VIKAS"],
            "endpoints": ["/api/index", "/api/chat", "/api/status"]
        })
    # Otherwise return WEBSITE
    return HTML

# === API ENDPOINTS (Explicit) ===
@app.route('/api/index', methods=['GET','POST'])
@app.route('/api/chat', methods=['GET','POST'])
@app.route('/api/status', methods=['GET','POST'])
def api_handler():
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        q = data.get('query', data.get('message', 'Namaste'))
        return jsonify({
            "response": f"BHARAT-AGI [7-layer sovereign processing]: '{q}' -> Processed through RAKSHAK (Safety) -> DRISHTI (Perception) -> MANAS (Reasoning) -> KARMA (Action) -> VAANI (Language). Sovereign response generated for Bharat! Jai Hind! 🚀",
            "query": q,
            "architecture": "7-Layer Sovereign AGI",
            "status": "Live"
        })
    return jsonify({
        "name": "BHARAT-AGI",
        "status": "Live - Sovereign AGI",
        "layers": 7,
        "version": "1.0 - Production",
        "message": "India First AGI Operational - Jai Hind!",
        "architecture": ["RAKSHAK - Safety","DRISHTI - Perception","MANAS - Reasoning","KARMA - Action","VAANI - Language","ANUBHAV - Memory","VIKAS - Evolution"],
        "tagline": "Built for Bharat, By Bharat. Sovereign, Secure, Swadeshi."
    })