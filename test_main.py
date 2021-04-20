from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}


def test_read_method_get():
    response = client.get("/method")
    assert response.status_code == 200
    assert response.json() == {"method": "GET"}

def test_read_method_put():
    response = client.put("/method")
    assert response.status_code == 200
    assert response.json() == {"method": "PUT"}

def test_read_method_delete():
    response = client.delete("/method")
    assert response.status_code == 200
    assert response.json() == {"method": "DELETE"}

def test_read_method_options():
    response = client.options("/method")
    assert response.status_code == 200
    assert response.json() == {"method": "OPTIONS"}

def test_read_method_post():
    response = client.post("/method")
    assert response.status_code == 201
    assert response.json() == {"method": "POST"}


def test_auth_1():
    password = "haslo"
    password_hash = "013c6889f799cd986a735118e1888727d1435f7f623d05d58c61bf2cd8b49ac90105e5786ceaabd62bbc27336153d0d316b2d13b36804080c44aa6198c533215"
    response = client.get(f"/auth?password={password}&password_hash={password_hash}")
    assert response.status_code == 204


def test_auth_2():
    password = "haslo"
    password_hash = "01as3c6889f799cd986a735118e1888727d1435f7f623d05d58c61bf2cd8b49ac90105e5786ceaabd62bbc27336153d0d316b2d13b36804080c44aa6198c533215"
    response = client.get(f"/auth?password={password}&password_hash={password_hash}")
    assert response.status_code == 401

def test_auth_3():
    response = client.get("/auth")
    assert response.status_code == 401

# @pytest.mark.parametrize("name", ["Zenek", "Marek", "Alojzy Niezdąży"])
# def test_hello_name(name):
#     response = client.get(f"/hello/{name}")
#     assert response.status_code == 200
#     assert response.text == f'"Hello {name}"'