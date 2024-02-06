from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.basic_models import BasicModel


class Donation(BasicModel):
    """Модель для пожертвований."""
    comment = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
