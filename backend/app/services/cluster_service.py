from sqlalchemy.orm import Session
from app.models.cluster import Cluster

class ClusterService:

    @staticmethod
    def create_cluster(db: Session, name: str):
        cluster = Cluster(name=name)
        db.add(cluster)
        db.commit()
        db.refresh(cluster)
        return cluster

    @staticmethod
    def list_clusters(db: Session):
        return db.query(Cluster).all()
