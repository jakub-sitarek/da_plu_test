from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import hashlib
from typing import Optional

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello world!"}

@app.get("/method")
def method_get():
    return {"method": "GET"}

@app.delete("/method")
def method_delete():
    return {"method": "DELETE"}

@app.put("/method")
def method_put():
    return {"method": "PUT"}

@app.options("/method")
def method_options():
    return {"method": "OPTIONS"}

@app.post("/method", status_code=201)
def method_put():
    return {"method": "POST"}

@app.get("/auth")
def auth(response: Response, password = None , password_hash = None):
    if password is None or password_hash is None:
        response.status_code = 401
        return
    hashed = hashlib.sha512(password.encode("utf-8")).hexdigest()
    if password_hash == hashed:
        response.status_code = 204
    else:
        response.status_code = 401