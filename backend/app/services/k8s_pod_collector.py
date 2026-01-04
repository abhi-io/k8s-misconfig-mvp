from app.core.k8s import get_k8s_client

def collect_pods():
    v1 = get_k8s_client()["core"]
    pod_list = v1.list_pod_for_all_namespaces().items

    pods = []

    for pod in pod_list:
        restart_count = sum(
            c.restart_count for c in (pod.status.container_statuses or [])
        )

        pods.append({
            "namespace": pod.metadata.namespace,
            "name": pod.metadata.name,
            "node_name": pod.spec.node_name,
            "phase": pod.status.phase,
            "restart_count": restart_count,
            "created_at": pod.metadata.creation_timestamp,
        })

    return pods
