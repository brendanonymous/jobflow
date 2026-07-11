from datetime import date, datetime
from typing import List
from sqlalchemy import BigInteger, Identity, ForeignKey, String, Date, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base

class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    company_name: Mapped[str] = mapped_column(String(100))
    role_name: Mapped[str] = mapped_column(String(200))

    user: Mapped["User"] = relationship(
        back_populates="applications"
    )

    status_events: Mapped[List["StatusEvent"]] = relationship(
        back_populates="application",
        cascade="all, delete-orphan",
    )

    applied_date: Mapped[date] = mapped_column(Date, server_default=func.current_date())
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now()
    )

    __table_args__ = (
        Index("idx_applications_user_id", "user_id"),
    )