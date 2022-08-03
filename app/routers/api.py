from fastapi import APIRouter

router = APIRouter()

@router.get("/echo")
async def health(text:str):
    return {"key": text}
