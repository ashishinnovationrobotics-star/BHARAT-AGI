from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Try to connect Supabase
try:
    from supabase import create_client
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    supabase = None
    if SUPABASE_URL and SUPABASE_KEY:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        print(f"✅ Supabase Connected: {SUPABASE_URL}")
    else:
        print("⚠️ Env vars not set")
except Exception as e:
    supabase = None
    print(f"Supabase error: {e}")

# Fallback local storage
local_data = [
    {"name": "Bharat", "content": "Bharat is a sovereign AI built in India. Ayurveda, Vedas, Yoga are Indian knowledge."}
]

def get_knowledge_base():
    if supabase:
        try:
            res = supabase.table("bharat_knowledge").select("*").execute()
            if res.data:
                return res.data
        except Exception as e:
            print(f"DB fetch error: {e}")
    return local_data

def search_knowledge(query):
    kb = get_knowledge_base()
    q = query.lower()
    results = []
    for item in kb:
        if any(word in item.get('content','').lower() or word in item.get('name','').lower() for word in q.split()):
            results.append(item)
    return results[:3]

@app.get("/", response_class=HTMLResponse)
async def home():
    status = "🟢 SOVEREIGN DB CONNECTED (Supabase)" if supabase else "🟡 LOCAL MODE (Add Env in Vercel)"
    count = len(get_knowledge_base())
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>BHARAT-AGI | Sovereign AI</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body{{font-family:system-ui; background:#0f172a; color:white; padding:20px; max-width:900px; margin:0 auto}}
            .card{{background:#1e293b; padding:20px; border-radius:12px; margin:15px 0; border:1px solid #334155}}
            input, textarea, button{{width:100%; padding:12px; margin:8px 0; border-radius:8px; border:none; font-size:16px}}
            textarea{{height:100px}}
            button{{background:#f59e0b; color:black; font-weight:bold; cursor:pointer}}
            button:hover{{background:#fbbf24}}
            .msg{{padding:10px; border-radius:8px; margin:10px 0}}
            .user{{background:#2563eb; text-align:right}}
            .bot{{background:#334155}}
            #chat{{max-height:400px; overflow-y:auto}}
            .status{{padding:10px; background:#064e3b; border-radius:8px; text-align:center; font-weight:bold}}
        </style>
    </head>
    <body>
        <h1>🇮🇳 BHARAT-AGI | Sovereign AI</h1>
        <div class="status">{status} | Docs: {count}</div>
        
        <div class="card">
            <h3>📤 Upload Your Own Data (Sovereign)</h3>
            <input id="docName" placeholder="Name e.g. Ayurveda">
            <textarea id="docContent" placeholder="Paste your knowledge here... e.g. Ayurveda has 3 doshas Vata Pitta Kapha..."></textarea>
            <button onclick="upload()">Upload to Sovereign DB</button>
            <div id="uploadStatus"></div>
        </div>

        <div class="card">
            <h3>💬 Chat with YOUR Data</h3>
            <div id="chat"></div>
            <input id="q" placeholder="Ask e.g. What is dosha? or Bharat kya hai?" onkeypress="if(event.key==='Enter')ask()">
            <button onclick="ask()">Ask Bharat</button>
        </div>

        <script>
        async function upload(){{
            const name=document.getElementById('docName').value;
            const content=document.getElementById('docContent').value;
            if(!name || !content){{alert('Fill both!'); return;}}
            document.getElementById('uploadStatus').innerText='Uploading...';
            const res=await fetch('/upload',{{method:'POST', headers:{{'Content-Type':'application/json'}}, body:JSON.stringify({{name, content}})}});
            const data=await res.json();
            document.getElementById('uploadStatus').innerText=data.message;
            document.getElementById('docName').value=''; document.getElementById('docContent').value='';
        }}
        async function ask(){{
            const query=document.getElementById('q').value;
            if(!query) return;
            const chat=document.getElementById('chat');
            chat.innerHTML+=`<div class='msg user'>${{query}}</div>`;
            document.getElementById('q').value='';
            const res=await fetch('/chat',{{method:'POST', headers:{{'Content-Type':'application/json'}}, body:JSON.stringify({{query}})}});
            const data=await res.json();
            chat.innerHTML+=`<div class='msg bot'><b>Bharat:</b> ${{data.answer}}<br><small>Source: ${{data.source}}</small></div>`;
            chat.scrollTop=chat.scrollHeight;
        }}
        </script>
    </body>
    </html>
    """

@app.post("/upload")
async def upload_doc(request: Request):
    body = await request.json()
    name = body.get("name")
    content = body.get("content")
    if supabase:
        try:
            supabase.table("bharat_knowledge").insert({"name": name, "content": content}).execute()
            return {"message": "✅ Uploaded to Sovereign DB (Supabase)!"}
        except Exception as e:
            return {"message": f"DB Error: {str(e)}"}
    else:
        local_data.append({"name": name, "content": content})
        return {"message": "✅ Uploaded to Local (Add Env vars in Vercel for Permanent DB)!"}

@app.post("/chat")
async def chat_api(request: Request):
    body = await request.json()
    query = body.get("query", "")
    
    results = search_knowledge(query)
    
    if results:
        context = "\\n".join([r.get('content','') for r in results])
        answer = f"Based on your sovereign data: {context[:500]}..."
        source = ", ".join([r.get('name','') for r in results])
    else:
        # Sovereign fallback
        if "bharat" in query.lower():
            answer = "Bharat-AGI is India's Sovereign AI. Your data stays in India, built for India. Jai Hind!"
        elif "ayurveda" in query.lower() or "dosha" in query.lower():
            answer = "I don't have that in your DB yet. Upload Ayurveda knowledge using the upload panel above, then I will answer from YOUR data."
        else:
            answer = f"You asked: '{query}'. Upload related knowledge first, then I will answer only from your sovereign DB. This is true sovereignty - no foreign LLM."
        source = "Sovereign Logic"
    
    # Log to DB
    if supabase:
        try:
            supabase.table("chat_history").insert({"query": query, "response": answer}).execute()
        except: pass

    return {"answer": answer, "source": source}
