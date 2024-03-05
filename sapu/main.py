from fastapi import FastAPI, Query, Header, Response
from typing import Annotated, Union
from pydantic import BaseModel

app = FastAPI()
items = ["Tシャツ", "スカート", "ブーツ", "コート"]


#データを取得したい→GET

@app.get("/sample/")
def read_sample(
    response: Response,
    authorization: Union[str, None] =Header(default=None)
):
    print(authorization)
    response.headers["custom-header"] = "12345"
    return {"message": "ヘッダー情報を取得しました"}
    

@app.get("/items/{item_id}/detail")
def read_item(item_id):
    return {"item_id": item_id, "item_name": "mouse"}
    
    
@app.get("/items")
def read_tools(skip: int = 0, limit: Annotated[int, Query(ge=1, le=10)] = 10):
    return {"items": items[skip : skip + limit]}


#データを送信したい→POST

class Item(BaseModel):
    name: str
    price: float
    description: Union[str, None] = None
    
    
@app.post("/items/")
def create_item(item: Item):
    print(f"データを登録します: {item.name}, {item.price}, {item.description}")
    return item