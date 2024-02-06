from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models import CharityProject


async def check_name_duplicate(
    project_name: str,
    session: AsyncSession
) -> None:
    """Проверка уникальности имени проекта."""
    project = await charity_project_crud.get_project_id(
        project_name, session
    )
    if project:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Проект с таким именем уже существует!'
        )


async def check_existence(
    project_id: int,
    session: AsyncSession
) -> CharityProject:
    """Проверка наличия проекта в DB."""
    project = await charity_project_crud.get(project_id, session)
    if project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'Проекта с ID {project_id} нет в БД!'
        )
    return project


def check_amount(obj, new_amount=None):
    """Проверка вложенных средств при update и delete."""
    invested = obj.invested_amount
    if new_amount:
        if invested > new_amount:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Сумма не может быть меньше внесённой!'
            )
    elif invested > 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='В проект были внесены средства, не подлежит удалению!'
        )
    return obj


def check_closed(obj):
    """Проверка статуса проекта """
    if obj.fully_invested:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Закрытый проект нельзя редактировать!'
        )
