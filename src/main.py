import os
from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI running on AWS Lambda and is executed in region " + os.env["AWS_REGION"] + ", using runtime environment " + os.env["AWS_EXECUTION_ENV"]}

@app.get("/items")
def read_item():
    return {"item_id": 1}

@app.post("/items")
async def create_item(item: Item):
    return item

lambda_handler = Mangum(app, lifespan="off")
