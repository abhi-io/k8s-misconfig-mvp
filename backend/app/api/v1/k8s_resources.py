from fastapi import APIRouter
from app.core.k8s import get_k8s_client

router = APIRouter(prefix="/k8s", tags=["kubernetes"])

@router.get("/namespaces")
def list_namespaces():
    v1 = get_k8s_client()["core"]
    return [ns.metadata.name for ns in v1.list_namespace().items]

@router.get("/deployments")
def list_deployments():
    apps = get_k8s_client()["apps"]
    deployments = apps.list_deployment_for_all_namespaces().items
    return [
        {
            "name": d.metadata.name,
            "namespace": d.metadata.namespace
        }
        for d in deployments
    ]

@router.get("/pods")
def list_pods():
    v1 = get_k8s_client()["core"]
    pods = v1.list_pod_for_all_namespaces().items
    return [
        {
            "name": p.metadata.name,
            "namespace": p.metadata.namespace,
            "status": p.status.phase
        }
        for p in pods
    ]
