from typing import Optional
from enum import Enum
from pydantic import BaseModel
from pydantic import Field
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

class ColorPelo(Enum):
    blanco = 'blanco'
    rojo = 'rojo'
    negro = 'negro'

class Persona(BaseModel):

    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=0,
        le=115
    )
    hair_color: Optional[ColorPelo] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

class Locasion(BaseModel):
    ciudad: str
    estado: str
    pais: str

prefijo_api = 'api'

@app.get("/")
def home():

    return {"hello": "data"}

@app.post('/'+prefijo_api+'/persona/new')
def crear_persona(persona: Persona = Body(...)):

    return persona

@app.get('/'+ prefijo_api +'/persona/detail')
def show_persona(
    name: Optional[str] = Query(
        None,
        min_length = 1,
        max_length = 50,
        title = "Nombre de la Persona",
        description = "Identificando el nombre de la persona"
        ),
    age: str = Query(
        ...,
        title = "Persona edad",
        description = "edad de lapersona"
        )
        ):
    return {name: age}

'''
validadores:    ge = >=
                le = <=
                gt = >
                lt = <
'''

@app.get('/'+ prefijo_api +'/persona/detail/{persona_id}}')
def show_persona(
    persona_id: int = Path(
        ...,
        gt=0,
        title = "id persona",
        description = "persona unica"
        )
):
    return {persona_id: 'siiiiiiiiiii'}

@app.put("/persona/{persona_id}")
def update_persona(
    persona_id: int = Path(
        ...,
        title="persona ID",
        description="id de una persona",
        gt=0
    ),
    persona: Persona = Body(...),
    locasion: Locasion = Body(...)
):
    resultado = persona.dict()
    resultado.update(locasion.dict())
    return resultado