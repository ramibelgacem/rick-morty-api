from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Detail": "First Endpoint"}
