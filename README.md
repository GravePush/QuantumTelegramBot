# Telegram Blog Bot & API Admin Panel

Проект включает:
- Telegram-бот для просмотра постов блога
- API с админкой для управления постами (создание, обновление, удаление)

---

## Функционал

### Бот
- Команда `/posts` — показывает список заголовков постов в виде кнопок
- При нажатии на кнопку с заголовком — показывает текст и дату создания поста
- Кнопка "Назад" возвращает к списку постов

### API
- CRUD операции с постами: создание, обновление, удаление, просмотр
- Документация API через Swagger UI и ReDoc (`/docs` и `/redoc`)
- Авторизация через JWT

---

## Технологии

- Python 3.12
- FastAPI — для API
- SQLAlchemy — ORM
- Alembic — миграции базы данных
- PostgreSQL — СУБД (можно заменить на SQLite, поменяв конфигурацию)
- aiogram — Telegram бот
- httpx — асинхронные запросы к API 
- python-dotenv — для загрузки конфигурации из `.env`

---

## Установка и запуск

### 1. Клонировать репозиторий
- git clone https://github.com/GravePush/QuantumTelegramBot.git
- cd yourrepo

### 2. Создать вирутальное окружение
- python3 -m venv venv
- source venv/bin/activate  # Linux/macOS
- venv\Scripts\activate     # Windows

### 3. Установить зависимости
- pip install -r requirements.txt

### 4. Создать базу данных PostgreSQL
Создайте файл .env и укажите все необходимые параметры:
- DB_USER=your_db_user
- DB_PASS=your_db_password
- DB_HOST=localhost
- DB_PORT=5432
- DB_NAME=your_db_name

- BOT_API=your_telegram_bot_token
- SECRET_KEY=your_secret_key_for_jwt
- ALGORITHM=HS256
- ACCESS_TOKEN_EXPIRE_MINUTES=30

Затем запустите python database_setup.py
Если не получается, попробуйте создать БД вручную, например через PgAdmin.

### 5. Применить миграции
- alembic upgrade head

### 6. Применить миграции
- Запустить FastAPI сервер - uvicorn api.main:app --reload
- API будет доступен по адресу: http://localhost:8000

- Запустить бота - telegram-bot/main.py
---
### Использование
  
- Через API создайте посты (через /posts endpoint, используя Swagger или curl).
- В Telegram отправьте боту команду /posts — он покажет список заголовков.
- Нажмите на заголовок, чтобы увидеть полный текст и дату создания.
- Для возврата нажмите кнопку "Назад".
