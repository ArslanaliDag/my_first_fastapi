from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

# uvicorn validate:app --reload --host 192.168.30.155

app = FastAPI(
    title="Валидация данных"
)

cats = [
    {"id": 1, "cat_name": "Пуся", "price": 1000, "mass": 2.3},
    {"id": 2, "cat_name": "Муся", "price": 1200, "mass": 3.0},
    {"id": 3, "cat_name": "Сяся", "price": 3000, "mass": 4.1},
    {"id": 4, "cat_name": "Сюся", "price": 4000, "mass": 2.1, "vaccinations": [
        {"vaccination_name": "КовиВак", "created_at": "2020-03-22"},
        {"vaccination_name": "ВакВак", "created_at": "2021-04-12"},
    ]},
]

class Vaccination(BaseModel):
    id: int
    vaccination_name: str = Field(max_length = 10)
    created_at: datetime

class Cat(BaseModel):
    id: int
    cat_name: str = Field(max_length = 6)
    price: int
    mass: float = Field(ge = 0)
    vaccination: Optional[List[Vaccination]]

@app.get("/cats/{cat_id}", response_model = List[Cat])
def get_cat(cat_id: int):
    return [cat for cat in cats if cat.get("id") == cat_id]

@app.post("/cats")
def add_cats(cat: List[Cat]):
    cats.extend(cat)
    return {"status": 200, "data": cats}
    