from typing import Union

from fastapi import FastAPI

import claimprocess.application
#import payments.application

import libdb


app = FastAPI()


@app.on_event('startup')
async def on_startup():
    await libdb.init_db()


@app.get('/')
async def read_root():
    return {'Hello': 'World'}


# Host two microservices in this server:

# /claims
app.include_router(claimprocess.application.router)

# /payments
#app.include_router(payments.application.router)

#--#
