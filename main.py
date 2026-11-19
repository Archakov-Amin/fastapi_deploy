from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Привет, FastAPI!"}

@app.get("/greet/{name}")
def name(name: str):
    if name == "admin":
        return "Здравствуйте, Администратор!"
    else:
        return f"Здравствуйте, {name}"

@app.get("/numbers/{number}")
def number(number: int):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

@app.get("/age/{age}")
def age(age: int):
    if age < 18:
        return "minor"
    elif age >= 18 and age <= 64:
        return "adult"
    else:
        return "senior"

@app.get("/calculator")
def calculate(a: int, b: int, operation: str):
    if operation == "add":
        return f"{a} + {b} = {a + b}"
    elif operation == "subtrack":
        return f"{a} - {b} = {a - b}"
    elif operation == "multiply":
        return f"{a} * {b} = {a * b}"
    else:
        return "Ошибка: неизвестная операция"

@app.get("/delivery")
def delivery(country: str, order_price: int):
    if country == "russia" and order_price >= 5000:
        return "Доставка: бесплатная"
    elif country == "russia" and order_price < 5000:
        return "Доставка: 500р"
    else:
        return "Доставка: 1500р"