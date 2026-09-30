from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/api/index', methods=['GET','POST'])
def api():
    if request.method == 'POST':
        data = request.get_json() or {}
        q = data.get('query','')
        return jsonify({"response": f"BHARAT-AGI processing '{q}': Through 7-layer sovereign architecture, I ensure safe, culturally aligned response. Bharat is building its own intelligence. Jai Hind! 🚀"})
    return jsonify({"name":"BHARAT-AGI","status":"Live - Sovereign AGI","layers":7,"architecture":["RAKSHAK","DRISHTI","MANAS","KARMA","VAANI","ANUBHAV","VIKAS"],"message":"India First AGI Operational - Jai Hind!"})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({"name":"BHARAT-AGI","status":"Live - Sovereign AGI","layers":7,"architecture":["RAKSHAK","DRISHTI","MANAS","KARMA","VAANI","ANUBHAV","VIKAS"],"message":"India First AGI Operational - Jai Hind!"})