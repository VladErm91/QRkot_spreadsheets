from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Donation, CharityProject
from app.models.basic_models import close_donation
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud


async def execute_investment_process(
    session: AsyncSession,
    investment_project: Union[CharityProject, Donation]
):
    """Инвестирование в незакрытые проекты"""
    project = await charity_project_crud.get_data_from_session(session)
    donation = await donation_crud.get_data_from_session(session)
    if not project or not donation:
        await session.commit()
        await session.refresh(investment_project)
        return investment_project

    balance = project.full_amount - project.invested_amount
    donation_value = donation.full_amount - donation.invested_amount
    if balance > donation_value:
        project.invested_amount += donation_value
        await close_donation(donation)
    elif balance == donation_value:
        await close_donation(project)
        await close_donation(donation)
    else:
        project.invested_amount += balance
        await close_donation(project)

    session.add(project)
    session.add(donation)
    await session.commit()
    await session.refresh(project)
    await session.refresh(donation)
    return await execute_investment_process(session, investment_project)