from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Stock Scanner API Running"}

@app.get("/best-stocks")
def best_stocks():
    return [
        {
            "stock": "RELIANCE",
            "signal": "BUY",
            "confidence": 8.7,
            "stop_loss": 2450,
            "target": 2580,
            "expected_hold_time": "4-7 Days",
            "strategy": "Swing Pullback"
        },
        {
            "stock": "INFY",
            "signal": "BUY",
            "confidence": 8.2,
            "stop_loss": 1510,
            "target": 1600,
            "expected_hold_time": "3-5 Days",
            "strategy": "EMA Trend"
        }
    ]
