from fastapi import FastAPI
from model.user_connection import UserConnection
from schema.user_schema import UserSchema

app = FastAPI()
conn = UserConnection()

@app.get("/")
def root():
    conn
    print(conn)
    return "Hola esta es una app con fastapi"

@app.get("/return_all")
def info():
    items = []
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["name"] = data[1]
        dictionary["phone"] = data[2]
        items.append(dictionary)
    return items


@app.post("/api/insert")
def insert(user_data: UserSchema):
    dict = user_data.dict()
    dict.pop("id")
    conn.write(dict)
    return dict


@app.delete("/api/delete/{$id}")
def delete (id: str):
    conn.delete(id)
    return f"Se ha eliminado ${id}"


@app.get("/api/user/{id}")
def get_one(id : str):
    item = []
    data = conn.read_one(id)
    print(data)
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["name"] = data[1]
    dictionary["phone"] = data[2]
    item.append(dictionary)

    return item