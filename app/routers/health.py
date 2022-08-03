""" Router for Health requests """
from fastapi import APIRouter
from ..config import health_message

router = APIRouter()

@router.get("/health")
async def health():
    """ Return pre-defined health message """
    return {"message": health_message}
    