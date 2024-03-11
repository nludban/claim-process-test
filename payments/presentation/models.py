from decimal import Decimal
from sqlmodel import SQLModel, Field


class PaymentBase(SQLModel):
    claim_id: int = Field(foreign_key='claim.id', unique=True)
    net_fee: Decimal = Field(decimal_places=2)


class Payment(PaymentBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class PaymentCreate(PaymentBase):
    pass
