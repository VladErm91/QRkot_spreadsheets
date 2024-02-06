from datetime import datetime

from sqlalchemy import Column, Integer, Boolean, DateTime

from app.core.db import Base


class BasicModel(Base):
    """Базовая модель для Donation и CharityProject"""

    __abstract__ = True
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime, nullable=True)

    def __repr__(self) -> str:
        return super().__repr__()


async def close_donation(self):
    """Закрытие пожертвований и завершение инвестиций"""
    self.invested_amount = self.full_amount
    self.fully_invested = True
    self.close_date = datetime.now()
    self.project_total_time = self.close_date - self.create_date
    return self
