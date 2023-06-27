from fastapi import APIRouter, HTTPException
from src.infra.sqlalchemy.config import database
import uuid

router = APIRouter(tags=["Produtos"])