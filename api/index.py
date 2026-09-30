from flask import Flask, jsonify
import os
app = Flask(__name__)

# Read index.html for website
try:
    with open(os.path.join(os.path.dirname(__file__), '../index.html'), 'r', encoding='utf-8') as f:
        HTML = f.read()
except:
    HTML = "<html><body style=background:#000;color:#fff;text-align:center;padding:50px><h1>BHARAT-AGI</h1><h2>LIVE - Sovereign AGI</h2><p>7 Layers: RAKSHAK | DRISHTI | MANAS | KARMA | VAANI | ANUBHAV | VIKAS</p><p>Jai Hind!</p></body></html>"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
    if 'api' in path:
        return jsonify({"name":"BHARAT-AGI","status":"Live - Sovereign AGI","layers":7,"message":"India First AGI Operational - Jai Hind!","architecture":["RAKSHAK","DRISHTI","MANAS","KARMA","VAANI","ANUBHAV","VIKAS"]})
    return HTML