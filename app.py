from fastapi import FastAPI, UploadFile
import whisper
import os

app = FastAPI()

model = whisper.load_model("tiny")

@app.get("/")
def home():
    return {"message": "Transcripto AI Running"}

@app.post("/transcribe")
async def transcribe(file: UploadFile):

    filepath = file.filename

    with open(filepath, "wb") as f:
        f.write(await file.read())

    result = model.transcribe(filepath)

    os.remove(filepath)

    return {
        "text": result["text"]
    }