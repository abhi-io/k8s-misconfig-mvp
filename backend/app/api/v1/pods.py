from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.k8s_pod_collector import collect_pods
from app.services.pod_service import PodService

router = APIRouter(prefix="/pods", tags=["pods"])

@router.post("/scan/{cluster_id}")
def scan_and_store_pods(
    cluster_id: int,
    db: Session = Depends(get_db)
):
    print("+++++++++++++++++++++++++++++=")
    pods = collect_pods()
    PodService.bulk_insert_pods(db, cluster_id, pods)

    return {
        "cluster_id": cluster_id,
        "pods_inserted": len(pods)
    }
