from fastapi import APIRouter
from app.api.v1 import health, k8s_resources

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(k8s_resources.router)
