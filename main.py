from fastapi import FastAPI

app = FastAPI(
    title="Первое приложение на FastAPI"
)

@app.get("/")
def hello():
    return "Ассаляму алейкум!"

users = [
    {"id": 1, "role": "admin", "name": "Даниял"},
    {"id": 2, "role": "user", "name": "Арсланали"},
    {"id": 3, "role": "smm", "name": "Аркадий"},
]

@app.get("/users/{user_id}")
def get_user(user_id:int):
    return [user for user in users if user.get("id") == user_id]

cats = [
    {"id": 1, "user_id": 1, "cat_name": "Пуся", "price": 1000, "mass": 2.3},
    {"id": 2, "user_id": 2, "cat_name": "Муся", "price": 1200, "mass": 3.0},
    {"id": 3, "user_id": 3, "cat_name": "Сяся", "price": 3000, "mass": 4.1},
]

@app.get("/cats/")
def get_user_cats(limit: int = 1, offset: int = 0):
    return cats[offset:][:limit]

@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}