from sqlalchemy.orm import Session
from app.models.pod import Pod
from app.services.k8s_pod_collector import collect_all_pods


def scan_and_store_all_pods(
    db: Session,
    cluster_id: int,
):
    print("🔍 Starting pod scan...")

    pods = collect_all_pods()
    total = len(pods)

    print(f"📦 Found {total} pods")

    # OPTIONAL: clear old snapshot (idempotent scan)
    db.query(Pod).filter(Pod.cluster_id == cluster_id).delete()
    db.commit()

    objects = []

    for index, pod in enumerate(pods, start=1):
        objects.append(
            Pod(
                cluster_id=cluster_id,
                namespace=pod["namespace"],
                name=pod["name"],
                node_name=pod["node_name"],
                phase=pod["phase"],
                restart_count=pod["restart_count"],
                k8s_uid=pod["k8s_uid"],
                k8s_created_at=pod["k8s_created_at"],
                raw_pod=pod["raw_pod"],
            )
        )

        if index % 10 == 0 or index == total:
            print(f"➡️  Processed {index}/{total} pods")

    db.bulk_save_objects(objects)
    db.commit()

    print("✅ Pod scan completed")
    return total
