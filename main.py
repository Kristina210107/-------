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

id_product = 3

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

@app.post("/products/" , tags=["Товары"])
async def add_product(data: dict):
    global id_product
    id: int = id_product
    if shop_db.get(id, None):
        shop_db[id] = data 
        id_product += 1
        return{"msg" : "Данные добавлены"}
    else:
        return{"err": "Такой товар существует!"}
@app.put("/products/{id}" , tags=["Товары"])
async def edit_product(id: int, data: dict):
    if shop_db.get(id, None):
        shop_db[id] = data 
        return{"msg" : "Данные добавлены"}
    else:
        return{"err": "Такой товар существует!"}
    
@app.delete("/products/{id}" , tags=["Товары"]) 
async def delete_products(id: int):
    if shop_db.get(id, None):
        del shop_db[id]     
        return{"msg" : f"Товар с id {id} обновлён"}
    return{"err": "Такой товар  не существует!"}

@app.put("/products/{id}" , tags=["Товары"])
async def edit_product(id:int, data: dict):
    if shop_db.get(id, None):
        shop_db[id] = data
        return{"msg" : f"Товар с id {id} обновлён"}
    return{"err": "Такой товар  не существует!"}

@app.patch("/products/{id}" , tags=["Товары"])
async def edit_product_partialy(id:int, data: dict):
    if shop_db.get(id, None):
        product = shop_db[id]
        for k,  v in data.items():
            if product.get(k, None):
                shop_db[id][k] = v

        return {"msg" : f"Товар с id {id} обновлён"}
    
    return {"err": "Такой товар  не существует!"}       