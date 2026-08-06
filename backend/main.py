import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Body, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from config import FILE_NAME
from gemini_client import get_answer_from_gemini
from db import Base, engine, get_user_requests, add_request_data

BASE_DIR = load_dotenv(FILE_NAME)

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    yield

app = FastAPI(
    title="Gusini 3.6 AI Assistant",
    lifespan=lifespan,
)

origins = [
    "http://localhost:5000",
    "https://shaurmasrepkoi.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/requests")
def get_my_requests(request: Request):
    user_ip_address = request.client.host
    print(f"{user_ip_address=}")
    user_requests = get_user_requests(ip_address=user_ip_address)
    return user_requests


@app.post("/requests")
def send_prompt(
        request: Request,
        prompt: str = Body(embed=True)
):
    user_ip_address = request.client.host
    answer = get_answer_from_gemini(prompt)
    add_request_data(
        ip_address=user_ip_address,
        prompt=prompt,
        response=answer,
    )
    return {"answer": answer}


@app.get("/")
def health_check():
    return {
        "status": "online",
        "service": "Gusini 3.6"
    }


