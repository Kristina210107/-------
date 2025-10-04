from fastapi import APIRouter

router = APIRouter(prefix="/products", tags = ["Продукы"])

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

@router.get("/" , tags=["Товары"])
async def get_products():
    return {"data" : shop_db}
@router.get("/{id}", tags=["Товары"])
async def get_produtc(id: int):
    if shop_db.get(id, None):
        return {"data" : shop_db[id]}
    else:
        return {"msg" : "Товара не существует"}
@router.post("/" , tags=["Товары"])
async def add_product(data: dict): 
    id = len(shop_db.keys())

    shop_db[id] = data  
    return {"msg" : "Товар добавлен"}
@router.post("/" , tags=["Товары"])
async def add_product(data: dict):
    global id_product
    id: int = id_product
    if shop_db.get(id, None):
        shop_db[id] = data 
        id_product += 1
        return{"msg" : "Данные добавлены"}
    else:
        return{"err": "Такой товар существует!"}
@router.put("/{id}" , tags=["Товары"])
async def edit_product(id: int, data: dict):
    if shop_db.get(id, None):
        shop_db[id] = data 
        return{"msg" : "Данные добавлены"}
    else:
        return{"err": "Такой товар существует!"}
@router.delete("/{id}" , tags=["Товары"]) 
async def delete_products(id: int):
    if shop_db.get(id, None):
        del shop_db[id]     
        return{"msg" : f"Товар с id {id} обновлён"}
    return{"err": "Такой товар  не существует!"}

@router.put("/{id}" , tags=["Товары"])
async def edit_product(id:int, data: dict):
    if shop_db.get(id, None):
        shop_db[id] = data
        return{"msg" : f"Товар с id {id} обновлён"}
    return{"err": "Такой товар  не существует!"}
@router.patch("/{id}" , tags=["Товары"])
async def edit_product_partialy(id:int, data: dict):
    if shop_db.get(id, None):
        product = shop_db[id]
        for k,  v in data.items():
            if product.get(k, None):
                shop_db[id][k] = v

        return {"msg" : f"Товар с id {id} обновлён"}
    
    return {"err": "Такой товар  не существует!"}       
