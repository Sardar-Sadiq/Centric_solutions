from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from analyzer import CaptionGenerator
import shutil
import os

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Initialize the AI engine once when the server starts
engine = CaptionGenerator()

@app.post("/caption")
async def get_caption(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Analyze
    result_text = engine.generate(temp_path)
    
    os.remove(temp_path) # Clean up
    return {"caption": result_text}