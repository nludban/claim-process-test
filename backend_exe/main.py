from typing import Union

from fastapi import FastAPI

import claimprocess.presentation.models
import payments.presentation.models

import libdb


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await libdb.init_db()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
