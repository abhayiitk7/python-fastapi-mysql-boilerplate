from fastapi.responses import JSONResponse
from fastapi import APIRouter,Depends
from typing import Any, Dict
from pydantic import BaseModel
import uvicorn
import logging
import json
import os
import pandas as pd
from sqlalchemy import text
from services.security import get_user_token

from db.connection import SqlConnector

sql_conn = SqlConnector()
# logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

class bureauReport(BaseModel):
    mobileNumber: int
    pan: str
    bureauResponse: Dict[str, Any]

sample_route = APIRouter()

@sample_route.post("/health")
def database_health():
     with sql_conn.engine.connect() as conn:
        print(f"Successfully connected to MySQL Server version")
        return {'database_health':"healthly"}



