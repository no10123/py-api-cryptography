from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

inventory = {
    1: {"name": "Keyboard", "price": 75.00, "in_stock": True}
}

@app.get("/")
def read_root():
    return {"message": "Welcome to your Python API"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in inventory:
        return {"error": "Item not found"}
    return inventory[item_id]

@app.post("/items/")
def create_item(item: Item):
    new_id = len(inventory) + 1
    inventory[new_id] = item.model_dump()
    return {"id": new_id, "item": inventory[new_id]}