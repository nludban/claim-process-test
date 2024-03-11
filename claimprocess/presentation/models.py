import datetime
from decimal import Decimal
from sqlmodel import SQLModel, Field, UniqueConstraint


class ClaimBase(SQLModel):
    service_date: datetime.date = Field(nullable=False)
    submitted_procedure: str = Field(nullable=False)
    quadrant: str = Field(nullable=True)
    plan_group_no: str = Field(nullable=False)
    subscriber_no: int = Field(nullable=False)
    provider_npi: str = Field(nullable=False)  # 10 digits.
    provider_fees: Decimal = Field(decimal_places=2, nullable=False)
    allowed_fees: Decimal = Field(decimal_places=2, nullable=False)
    member_coinsurance: Decimal = Field(decimal_places=2, nullable=False)
    member_copay: Decimal = Field(decimal_places=2, nullable=False)

    status: str = Field(default='pending', nullable=False)  # pending, processed, failed.


class Claim(ClaimBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)

    __table_args__ = (
        UniqueConstraint('provider_npi',
                         'plan_group_no',
                         'subscriber_no',
                         'service_date',
                         'submitted_procedure',
                         name='unique_claim_id'),
    )


class ClaimCreate(ClaimBase):
    pass
