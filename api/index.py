from fastapi import FastAPI
app = FastAPI()

@app.get("/api")
def root():
    return {"status": "Bharat AGI Backend Live 3026 - Python + HTML Hybrid Works", "mode": "hybrid"}

@app.get("/api/health")
def health():
    return {"core": "online", "bharat": "ready"}
