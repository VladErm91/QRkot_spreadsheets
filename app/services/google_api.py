import copy

from aiogoogle import Aiogoogle
from datetime import datetime
from typing import List, Dict

from app.core.config import settings

FORMAT = "%Y/%m/%d %H:%M:%S"
TITLE = 'Projects'
JS_CONST = dict(
    properties=dict(
        title='Отчет от ',
        locale='ru_RU',
    ),
    sheets=[dict(properties=dict(
        sheetType='GRID',
        sheetId=0,
        title=TITLE,
    ))]
)
TABLE_HEADERS = [
    ['Отчет от'],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание'],
]


async def spreadsheets_create(
        wrapper_services: Aiogoogle,
        projects_count: int,
        spreadsheet_body: Dict = None
) -> List:
    spreadsheet_body = (
        spreadsheet_body if spreadsheet_body else copy.deepcopy(JS_CONST)
    )
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')

    spreadsheet_body['properties']['title'] += now_date_time
    spreadsheet_body['sheets'][0]['properties'].update(dict(
        gridProperties=dict(
            rowCount=projects_count + len(TABLE_HEADERS),
            columnCount=len(TABLE_HEADERS[-1]),
        )
    ))

    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheet_id = response['spreadsheetId']
    return [spreadsheet_id, now_date_time]


async def set_user_permissions(
        wrapper_services: Aiogoogle,
        spreadsheet_id: str,
) -> None:
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email_user}
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        wrapper_services: Aiogoogle,
        spreadsheet_id: str,
        projects: List,
        spreadsheet_creation_date: str,
        table_header: List = None,
) -> None:
    service = await wrapper_services.discover('sheets', 'v4')
    table_header = table_header if table_header else copy.deepcopy(
        TABLE_HEADERS
    )
    table_header[0].append(spreadsheet_creation_date)
    table_values = [
        *table_header,
        *[list(map(str, project)) for project in projects]
    ]
    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=TITLE,
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
