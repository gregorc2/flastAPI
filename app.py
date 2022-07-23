from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import Body



app = FastAPI()

class Persona(BaseModel):

    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None



prefijo_api = 'api'

@app.get("/")
def home():

    return {"hello": "data"}

@app.post('/'+prefijo_api+'/persona/new')
def crear_persona(persona: Persona = Body(...)):

    return persona