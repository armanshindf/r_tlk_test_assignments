from fastapi import FastAPI, Depends
from pydantic import BaseModel


app = FastAPI()

class Parse(BaseModel):
    name: str
    age: int


@app.post('/parse/')
async def parse_request(parse: Parse):
    return parse

@app.get('/ping')
async def ping():
    return {'ping': 'pong!'}