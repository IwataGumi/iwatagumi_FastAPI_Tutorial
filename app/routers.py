from typing import List
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


@router.post("/")
async def hello_world():
    return "Hello World!"
