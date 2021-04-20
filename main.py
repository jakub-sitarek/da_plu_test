from fastapi import FastAPI, Response, status

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

