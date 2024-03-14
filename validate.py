from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

# uvicorn validate:app --reload --host 192.168.30.155

app = FastAPI(
    title="Валидация данных"
)

class Cat(BaseModel):
    id: int
    cat_name: str
    price: int
    mass: float

cats = [
    {"id": 1, "cat_name": "Пуся", "price": 1000, "mass": 2.3},
    {"id": 2, "cat_name": "Муся", "price": 1200, "mass": 3.0},
    {"id": 3, "cat_name": "Сяся", "price": 3000, "mass": 4.1},
]

@app.post("/cats")
def add_cats(cat: List[Cat]):
    cats.extend(cat)
    return {"status": 200, "data": cats}


    