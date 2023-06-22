from fastapi import APIRouter, HTTPException
from infra.sqlalchemy.config.database import *
import uuid

router = APIRouter(tags=["Produtos"])