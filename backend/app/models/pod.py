from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey, Index
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from app.core.database import Base


class Pod(Base):
    __tablename__ = "pods"

    id = Column(Integer, primary_key=True)

    cluster_id = Column(
        Integer,
        ForeignKey("clusters.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    namespace = Column(String, index=True)
    name = Column(String, index=True)
    node_name = Column(String, index=True)
    phase = Column(String, index=True)

    restart_count = Column(Integer, default=0)

    k8s_uid = Column(String, index=True)
    k8s_created_at = Column(DateTime)

    scanned_at = Column(DateTime, server_default=func.now())

    # 🔑 FULL POD OBJECT (future-proof)
    raw_pod = Column(JSONB, nullable=False)

    __table_args__ = (
        Index(
            "idx_pods_cluster_namespace_name",
            "cluster_id",
            "namespace",
            "name",
        ),
    )
