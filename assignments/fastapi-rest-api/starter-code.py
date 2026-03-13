# Starter Code for FastAPI REST API Assignment

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Example in-memory storage for items
items = []
next_id = 1

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    completed: bool = False

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

@app.post("/items/", status_code=201)
def create_item(item: Item):
    global next_id
    item.id = next_id
    next_id += 1
    items.append(item)
    return item

@app.get("/items/", response_model=List[Item])
def list_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            updated.id = item_id
            items[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return
    raise HTTPException(status_code=404, detail="Item not found")
