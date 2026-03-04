from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from parser import get_pdf_text
from analyzer import ResumeReviewer
import shutil

app = FastAPI()

# Enable CORS so Bun (frontend) can talk to Python (backend)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/review")
async def review_resume(file: UploadFile = File(...)):
    # Save file temporarily
    path = f"temp_{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Process
    text = get_pdf_text(path)
    reviewer = ResumeReviewer(text)
    results = reviewer.get_score(["React", "Python", "Tailwind", "JavaScript"])
    
    return results