from fastapi import FastAPI
from routers import api, health

server = FastAPI()
server.include_router(health.router, prefix="/-")
server.include_router(api.router, prefix="/api")