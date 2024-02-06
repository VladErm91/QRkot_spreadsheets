from sqlalchemy import Column, Interval, String, Text

from app.models.basic_models import BasicModel


class CharityProject(BasicModel):
    """Модель для целевых проектов."""
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    project_total_time = Column(Interval, default=None)
