from fastapi import APIRouter
from config import health_message

router = APIRouter()

@router.get("/health")
async def health():
    return health_message