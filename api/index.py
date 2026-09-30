from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "name": "BHARAT-AGI",
        "status": "Live - Sovereign AGI",
        "layers": 7,
        "message": "India First AGI Operational - Jai Hind!"
    })

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    q = data.get("query","Namaste")
    return jsonify({
        "rakshak": "Safe",
        "perception": q,
        "core_reasoning": f"Bharat AGI processing: {q}",
        "response": f"BHARAT-AGI: {q} - Jai Hind!"
    })

@app.route("/<path:path>")
def catch_all(path):
    return home()
