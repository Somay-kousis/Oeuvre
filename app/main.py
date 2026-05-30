from fastapi import FastAPI
from pydantic import BaseModel
from app.chat import ask

app = FastAPI()


class AskRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"status": "Portfolio AI backend is running"}


@app.post("/ask")
def ask_route(request: AskRequest):
    answer = ask(request.question)
    return {"answer": answer}