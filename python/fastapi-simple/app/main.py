from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "FastAPI 🚀"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/plusone/{item_id}")
def read_item(item_id: int):
    q: int = item_id + 1
    return {"item_id": item_id, "plusone": q}
