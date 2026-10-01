from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"status": "Bharat AGI Backend Live 3026 - Python + HTML Hybrid Works"}

@app.get("/api")
def api_root():
    return {"message": "api working"}
