from datetime import datetime
from sqlalchemy import BigInteger, Index, Identity, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base

class StatusEvent(Base):
    __tablename__ = "status_events"

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True), primary_key=True)

    application_id: Mapped[int] = mapped_column(
        ForeignKey("applications.id", ondelete="CASCADE")
    )

    application: Mapped["Application"] = relationship(
        back_populates="status_events"
    )
    status: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    __table_args__ = (
        Index("idx_status_events_application_id", "application_id"),
    )