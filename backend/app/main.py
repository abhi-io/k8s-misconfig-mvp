from fastapi import FastAPI
from app.core.database import Base, engine

# 👇 THIS IS REQUIRED
from app.models.cluster import Cluster  # noqa: F401
from app.models.pod import Pod  # noqa: F401

from app.api.v1.router import api_router

app = FastAPI(title="K8s Misconfig MVP")

Base.metadata.create_all(bind=engine)

app.include_router(api_router)
