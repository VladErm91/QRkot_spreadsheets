from datetime import timedelta
from typing import Optional, Dict, List, Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id(
        self,
        project_name: str,
        session: AsyncSession
    ) -> Optional[int]:
        """Получение id проекта по имени."""
        project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        return project_id.scalars().first()

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> List[Dict[str, Union[str, timedelta]]]:
        projects = await session.execute(
            select([
                CharityProject.name,
                CharityProject.project_total_time,
                CharityProject.description
            ]).where(
                CharityProject.fully_invested.is_(True)
            ).order_by(CharityProject.project_total_time)
        )
        return projects.all()


charity_project_crud = CRUDCharityProject(CharityProject)