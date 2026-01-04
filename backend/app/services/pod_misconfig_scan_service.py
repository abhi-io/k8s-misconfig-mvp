from sqlalchemy.orm import Session
from app.models.pod import Pod
from app.models.finding import Finding
from app.engine.rule_loader import load_rules
from app.engine.pod_detection_engine import evaluate_rule


def scan_pods_for_misconfigurations(
    db: Session,
    cluster_id: int,
    rule_dir: str = "rules/pods",
):
    rules = load_rules(rule_dir)

    pods = db.query(Pod).filter(Pod.cluster_id == cluster_id).all()
    print(f"🔎 Scanning {len(pods)} pods against {len(rules)} rules")

    findings = []

    for pod in pods:
        for rule in rules:
            if evaluate_rule(pod.raw_pod, rule):
                findings.append(
                    Finding(
                        cluster_id=cluster_id,
                        pod_id=pod.id,
                        rule_id=rule["id"],
                        severity=rule["severity"],
                        title=rule["title"],
                        description=rule["description"],
                        root_cause=rule["root_cause"],
                        mitigation=rule["mitigation"],
                    )
                )

    db.bulk_save_objects(findings)
    db.commit()

    print(f"🚨 Detected {len(findings)} findings")
    return len(findings)
