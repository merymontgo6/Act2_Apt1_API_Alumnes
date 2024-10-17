from fastapi import FastAPI, HTTPException
import db_alumnat
import alumnes
from typing import List

from pydantic import BaseModel

app = FastAPI()

class alumne(BaseModel):
    idAula: int
    nomAlumne: str
    cicle: str
    curs: str
    grup: str