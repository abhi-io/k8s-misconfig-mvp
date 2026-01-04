from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
# from app.services.k8s_pod_collector import collect_pods
from app.services.pod_service import PodService
from app.services.pod_scan_service import scan_and_store_all_pods

router = APIRouter(prefix="/pods", tags=["pods"])


@router.post("/scan/{cluster_id}")
def scan_pods(cluster_id: int, db: Session = Depends(get_db)):
    count = scan_and_store_all_pods(db, cluster_id)
    return {
        "cluster_id": cluster_id,
        "pods_scanned": count,
    }
