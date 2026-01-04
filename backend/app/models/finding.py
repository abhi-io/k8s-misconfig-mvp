# Database model for findings
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from app.core.database import Base


class Finding(Base):
    __tablename__ = "findings"

    id = Column(Integer, primary_key=True)

    cluster_id = Column(Integer, ForeignKey("clusters.id"), index=True)
    pod_id = Column(Integer, ForeignKey("pods.id"), index=True)

    rule_id = Column(String, index=True)
    severity = Column(String, index=True)

    title = Column(String)
    description = Column(Text)
    root_cause = Column(Text)
    mitigation = Column(Text)

    detected_at = Column(DateTime, server_default=func.now())
