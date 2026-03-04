from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from analyzer import ResumeAnalyzer
import os

app = FastAPI()

#allow react to talk to python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_origins=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    # 1. save file temporarily
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 2. Process with our class 
    target_keywords = ["React", "Python", "SQL", "API"]
    engine = ResumeAnalyzer(temp_path)

    if engine.extract_content():
        results = engine.analyze(target_keywords)
        os.remove(temp_path)
        return results

    return {"error": "failed to process file"}