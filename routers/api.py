from fastapi import APIRouter
from ..config import health_message

router = APIRouter()

@router.get("/echo")
async def health(text:str):
    return {"key": text}
