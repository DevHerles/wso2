from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import socket

app = FastAPI()

# In-memory storage
fake_items_db = {}

@app.get("/")
async def read_root():
    hostname = socket.gethostname()
    return {"message": "Hello, world!", "hostname": hostname}

# Model for Item
class Item(BaseModel):
    name: str
    description: str = None

# CRUD Operations

# Create an item
@app.post("/items/")
async def create_item(item: Item):
    fake_items_db[item.name] = item
    return item

# Read an item
@app.get("/items/{name}")
async def read_item(name: str):
    if name not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_items_db[name]

# Update an item
@app.put("/items/{name}")
async def update_item(name: str, item: Item):
    if name not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_items_db[name] = item
    return item

# Delete an item
@app.delete("/items/{name}")
async def delete_item(name: str):
    if name not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_items_db[name]
    return {"message": "Item deleted successfully"}

# List all items
@app.get("/items/")
async def list_items():
    return list(fake_items_db.values())
