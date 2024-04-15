# Приложение для благотворительного фонда поддержки котиков QRKot на основе Fast API c поддержкой Google Sheets.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Google](https://img.shields.io/badge/google-4285F4?style=for-the-badge&logo=google&logoColor=white)

### Возможности сервиса:

Создать приложение для организации сбора пожертвования котикам 
на различные цели к примеру на лечение, корм, создание благоприятных условий существования,
с поддержкой вывода отчетов по пожертвованиям на завершеннные проекты на основе Google Sheets

### Технологии проекта
* Python
* Fast API - отдельный фреймворк для работы с веб сайтами.
* Google API - отдельный фреймворк позволяющий подключаться и использовать различные сервисы Google например Google Sheets.

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/VladErm91/QRkot_spreadsheets.git

cd QRkot_spreadsheets
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запуск сервиса 

```
uvicorn app.main:app
```

### Необходимые переменные среды (.env)

Переменные для работы приложения
```
APP_TITLE=Приложение QRKot.
APP_DESC=
DATABASE_URL=
SECRET=

FIRST_SUPERUSER_EMAIL=
FIRST_SUPERUSER_PASSWORD=
```
Переменные для Google-API
```
EMAIL=
AUTH_PROVIDER_X509_CERT_URL=
AUTH_URI=
CLIENT_EMAIL=
CLIENT_ID=
CLIENT_X509_CERT_URL=
PRIVATE_KEY=
PRIVATE_KEY_ID=
PROJECT_ID=
TOKEN_URI=
TYPE=
```


Автор: [VladErm91](https://github.com/VladErm91)
