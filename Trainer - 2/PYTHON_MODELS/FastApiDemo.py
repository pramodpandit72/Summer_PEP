from fastapi import FastAPI
from transformers import pipeline
import torch
from pydantic import BaseModel   # to run-> uvicorn FastApiDemo:app --reload

app = FastAPI(
    title="FAST API APP",
    description="A FAST API PROJECT",
    version="1.0"
)

generator = pipeline("text-generation",
                    model="openai-community/gpt2")

@app.get("/")
def home():
    return {
        "message": "Welcome to GPT 2 FASTAPI",
        "status": "Running"
    }

class Prompt(BaseModel):
    prompt:str
    max_new_tokens:int=100

@app.post("/generate")
def generate_text(data:Prompt):
    result=generator(
        data.prompt,
        max_new_tokens=data.max_new_tokens,
    )
    return {
        "prompt": data.prompt,
        "generated_text": result[0][generated_text]
    }