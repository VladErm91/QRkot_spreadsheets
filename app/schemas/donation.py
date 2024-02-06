from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, PositiveInt


class DonationCreate(BaseModel):
    """Схема для создания пожертвования."""
    full_amount: PositiveInt
    comment: Optional[str]

    class Config:
        extra = Extra.forbid
        orm_mode = True


class DonationView(DonationCreate):
    """Схема для вывода информации по пожертвованию."""
    id: int
    create_date: datetime


class DonationDB(DonationView):
    """Схема со всеми полями по."""
    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]