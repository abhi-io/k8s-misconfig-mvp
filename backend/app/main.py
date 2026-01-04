from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="K8s Misconfig MVP")

app.include_router(api_router)
