import enum
import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Enum, ForeignKey, String, TIMESTAMP, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model import Base

if TYPE_CHECKING:
    from .user import User


class ReportType(str, enum.Enum):
    LOST = "LOST"
    FOUND = "FOUND"


class Item(Base):
    __tablename__ = "items"

    itemId: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    brand: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    color: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    model: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    lastSeenVenue: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    lastSeenTime: Mapped[Optional[datetime]] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=True,
    )
    uniqueIdentifier: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )
    reportType: Mapped[ReportType] = mapped_column(
        Enum(ReportType, name="report_type_enum"),
        nullable=False,
    )
    reporterId: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("users.userId"),
        nullable=False,
    )

    reporter: Mapped["User"] = relationship(
        "User",
        back_populates="reported_items",
    )