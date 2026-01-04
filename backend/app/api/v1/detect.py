from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.pod_misconfig_scan_service import (
    scan_pods_for_misconfigurations
)

router = APIRouter(prefix="/detect", tags=["detection"])


@router.post("/pods/{cluster_id}")
def detect_pod_misconfigs(cluster_id: int, db: Session = Depends(get_db)):
    count = scan_pods_for_misconfigurations(db, cluster_id)
    return {
        "cluster_id": cluster_id,
        "findings": count
    }
