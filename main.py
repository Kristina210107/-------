from fastapi import FastAPI, HTTPException
app = FastAPI(title="MyShop", version="0.0.1")

shop_db ={
    0 : {
        "name" : "Шампунь",
        "quantity": 3,
        "price" : 100
    },
    1 : {
        "name" : "Пицца",
        "quantity": 30,
        "price" : 500
    },
    2 : {
        "name" : "Вода",
        "quantity": 10,
        "price" : 50
    },
}



@app.get("/" , tags=["Магазин"])
async def home():
    return {"data" : "Welcome to my Shop"}

@app.get("/products/" , tags=["Товары"])
async def get_products():
    return {"data" : shop_db}

@app.get("/products/{id}" , tags=["Товары"])
async def get_product(id: int):
    if shop_db.get(id, None):
        return {"data" : shop_db[id]}
    else:
        raise HTTPException(status_code = 404, detail="Товара не существует")

@app.post("/products/" , tags=["Товары"])
async def add_product(data: dict): 
    id = len(shop_db.keys())

    shop_db[id] = data  
    return {"msg" : "Товар добавлен"}

@app.post("/products/{id}" , tags=["Товары"])
async def add_product(data: dict):
    id: int = len(shop_db.keys())
    if shop_db.get(id, None):
        shop_db[id] = data 
        return{"msg" : "Данные добавлены"}
    else:
        return{"err": "Такой товар существует!"}