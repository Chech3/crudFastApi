from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from model.user_connection import UserConnection
from schema.user_schema import UserSchema

app = FastAPI()
conn = UserConnection()

@app.get("/")
def root():
    conn
    print(conn)
    return "Hola esta es una app con fastapi"

@app.get("/return_all", status_code=HTTP_200_OK)
def info():
    items = []
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["name"] = data[1]
        dictionary["phone"] = data[2]
        items.append(dictionary)
    return items


@app.post("/api/insert", status_code=HTTP_201_CREATED)
def insert(user_data: UserSchema):
    dict = user_data.dict()
    dict.pop("id")
    conn.write(dict)
    return Response(status_code=HTTP_201_CREATED)


@app.delete("/api/delete/{id}", status_code=HTTP_204_NO_CONTENT)
def delete (id: str):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

@app.put("/api/update/{id}", status_code=HTTP_204_NO_CONTENT)
def update (user_data: UserSchema, id: str):
    data = user_data.dict()
    data["id"] = id
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.get("/api/user/{id}", status_code=HTTP_200_OK)
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