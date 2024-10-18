from fastapi import FastAPI, HTTPException
import db_alumnat
import alumnes
from typing import List

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class tablaAlumne(BaseModel):
    nomAlumne: str
    cicle: str
    curs: str
    grup: str
    descAula: int

@app.get("/")
def read_root():
    return {"Alumnes API"} 

# Retorna una llista json amb tota la informació d’alumnes
@app.get("/alumne/listAll", response_model=List[tablaAlumne])
def read_all_alumnes():
    alumnes = db_alumnat.fetch_all_alumnes()
    print(alumnes)  # Crida al mètode per recuperar alumnes

    if not alumnes or (isinstance(alumnes, dict) and 'status' in alumnes):  # Comprova si hi ha un error
        raise HTTPException(status_code=404, detail="No hi ha alumnes enregistrats")
    
    return alumnes