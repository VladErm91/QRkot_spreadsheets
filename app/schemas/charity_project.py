from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt


class CharityProjectUpdate(BaseModel):
    """Схема для обновления проекта."""
    name: str = Field(None, max_length=100)
    description: str = Field(None, )
    full_amount: Optional[PositiveInt]

    class Config:
        min_anystr_length = 1
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectUpdate):
    """Схема для создания проекта."""
    name: str = Field(..., max_length=100)
    description: str = Field(..., )
    full_amount: PositiveInt


class CharityProjectDB(CharityProjectCreate):
    """Схема со всеми данными проекта."""
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True