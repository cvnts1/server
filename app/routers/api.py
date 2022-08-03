""" Router for API requests """

from fastapi import APIRouter

router = APIRouter()

@router.get("/echo")
async def health(text:str):
    """ Return given text """
    return {"key": text}
