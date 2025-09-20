from fastapi import FastAPI

app: Any = FastAPI()

@app.get("/")
async def home():
    return{"value": "Hello world!"}