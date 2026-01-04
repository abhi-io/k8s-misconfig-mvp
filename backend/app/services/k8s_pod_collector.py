from kubernetes.client import ApiClient
from app.core.k8s import get_k8s_client


def collect_all_pods():
    v1 = get_k8s_client()["core"]
    api_client = ApiClient()

    pod_list = v1.list_pod_for_all_namespaces().items

    collected = []

    for pod in pod_list:
        restart_count = sum(
            c.restart_count
            for c in (pod.status.container_statuses or [])
        )

        collected.append({
            "namespace": pod.metadata.namespace,
            "name": pod.metadata.name,
            "node_name": pod.spec.node_name,
            "phase": pod.status.phase,
            "restart_count": restart_count,
            "k8s_uid": pod.metadata.uid,
            "k8s_created_at": pod.metadata.creation_timestamp,
            # 👇 FULL RAW POD (converted to dict)
            "raw_pod": api_client.sanitize_for_serialization(pod),
        })

    return collected
