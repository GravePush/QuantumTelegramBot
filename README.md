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

```bash
git clone https://github.com/GravePush/QuantumTelegramBot.git
cd yourrepo

### 2. Создать вирутальное окружение
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

### 3. Установить зависимости
```bash
pip install -r requirements.txt

