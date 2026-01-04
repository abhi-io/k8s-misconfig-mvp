from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class Pod(Base):
    __tablename__ = "pods"

    id = Column(Integer, primary_key=True, index=True)

    cluster_id = Column(Integer, ForeignKey("clusters.id"), nullable=False)

    namespace = Column(String, index=True)
    name = Column(String, index=True)
    node_name = Column(String)
    phase = Column(String)

    restart_count = Column(Integer, default=0)

    k8s_created_at = Column(DateTime)
    scanned_at = Column(DateTime, server_default=func.now())
