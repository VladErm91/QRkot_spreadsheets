from aiogoogle import Aiogoogle
from datetime import timedelta
from typing import Dict, List, Union
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.services.google_api import (
    spreadsheets_create, set_user_permissions, spreadsheets_update_value
)

router = APIRouter()


@router.post(
    '/',
    response_model=List[Dict[str, Union[str, timedelta]]],
    dependencies=[Depends(current_superuser)],
)
async def get_report(
        session: AsyncSession = Depends(get_async_session),
        wrapper_services: Aiogoogle = Depends(get_service)

):
    """Только для суперюзеров."""
    projects = await charity_project_crud.get_projects_by_completion_rate(
        session
    )
    spreadsheet_id, spreadsheet_creation_date = await spreadsheets_create(
        wrapper_services, len(projects)
    )
    await set_user_permissions(wrapper_services, spreadsheet_id)
    await spreadsheets_update_value(
        wrapper_services, spreadsheet_id, projects, spreadsheet_creation_date
    )
    return projects