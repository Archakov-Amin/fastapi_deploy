import os
import psycopg2
import redis
from fastapi import FastAPI, HTTPException

app = FastAPI(title="FastAPI Backend Project")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/app_db")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

@app.get("/")
def root():
    return {"message": "Привет, FastAPI!"}

@app.get("/health")
def health_check():
    status = {"app": "ok", "db": "error", "redis": "error"}
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        status["db"] = "connected"
    except Exception as e:
        status["db_error"] = str(e)

    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, socket_connect_timeout=2)
        if r.ping():
            status["redis"] = "connected"
    except Exception as e:
        status["redis_error"] = str(e)

    if status["db"] != "connected" or status["redis"] != "connected":
        raise HTTPException(status_code=503, detail=status)
        
    return status

@app.get("/greet/{name}")
def greet(name: str):
    if name == "admin":
        return "Здравствуйте, Администратор!"
    return f"Здравствуйте, {name}"

@app.get("/numbers/{number}")
def check_number(number: int):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    return "zero"

@app.get("/age/{age}")
def check_age(age: int):
    if age < 18:
        return "minor"
    elif 18 <= age <= 64:
        return "adult"
    return "senior"

@app.get("/calculator")
def calculate(a: int, b: int, operation: str):
    if operation == "add":
        return f"{a} + {b} = {a + b}"
    elif operation == "subtract":
        return f"{a} - {b} = {a - b}"
    elif operation == "multiply":
        return f"{a} * {b} = {a * b}"
    return "Ошибка: неизвестная операция"

@app.get("/delivery")
def delivery(country: str, order_price: int):
    if country == "russia" and order_price >= 5000:
        return "Доставка: бесплатная"
    elif country == "russia" and order_price < 5000:
        return "Доставка: 500р"
    return "Доставка: 1500р"