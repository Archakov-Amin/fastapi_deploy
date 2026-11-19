from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Привет, FastAPI!"}

def test_greet():
    assert client.get("/greet/admin").json() == "Здравствуйте, Администратор!"
    assert client.get("/greet/Иван").json() == "Здравствуйте, Иван"

def test_numbers():
    assert client.get("/numbers/10").json() == "positive"
    assert client.get("/numbers/-5").json() == "negative"
    assert client.get("/numbers/0").json() == "zero"

def test_age():
    assert client.get("/age/10").json() == "minor"
    assert client.get("/age/25").json() == "adult"
    assert client.get("/age/70").json() == "senior"

def test_calculator():
    assert client.get("/calculator?a=5&b=3&operation=add").json() == "5 + 3 = 8"
    assert client.get("/calculator?a=5&b=3&operation=subtrack").json() == "5 - 3 = 2"
    assert client.get("/calculator?a=5&b=3&operation=multiply").json() == "5 * 3 = 15"
    assert client.get("/calculator?a=5&b=3&operation=div").json() == "Ошибка: неизвестная операция"

def test_delivery():
    assert client.get("/delivery?country=russia&order_price=6000").json() == "Доставка: бесплатная"
    assert client.get("/delivery?country=russia&order_price=1000").json() == "Доставка: 500р"
    assert client.get("/delivery?country=usa&order_price=6000").json() == "Доставка: 1500р"
