from sqlalchemy.orm import Session
from app.models.pod import Pod

class PodService:

    @staticmethod
    def bulk_insert_pods(db: Session, cluster_id: int, pods: list[dict]):
        pod_objects = []

        for pod in pods:
            pod_objects.append(
                Pod(
                    cluster_id=cluster_id,
                    namespace=pod["namespace"],
                    name=pod["name"],
                    node_name=pod.get("node_name"),
                    phase=pod["phase"],
                    restart_count=pod["restart_count"],
                    k8s_created_at=pod["created_at"],
                )
            )

        db.bulk_save_objects(pod_objects)
        db.commit()
