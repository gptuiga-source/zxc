# Telegram chat bot

An asynchronous Telegram chat bot built with `pyTelegramBotAPI` and Tortoise ORM. User records are stored in a local SQLite database (`bot_database.db`).

## Setup

1. Use Python 3.10 or newer.
2. Create and activate a virtual environment.
3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and set `TELEGRAM_BOT_TOKEN` to a newly issued token from BotFather.
5. Run:

   ```powershell
   python main.py
   ```

The bot loads its token from `.env` with `python-dotenv`. Do not commit `.env`. The token previously embedded in the source was exposed; revoke it in BotFather and use a newly issued token.

## Run with Docker

1. Copy `.env.example` to `.env` and put your newly issued token in `TELEGRAM_BOT_TOKEN`.
2. Build and start the bot:

   ```powershell
   docker compose up -d --build
   ```

3. View logs:

   ```powershell
   docker compose logs -f
   ```

Stop the bot with `docker compose down`. The named `bot-data` volume keeps the SQLite database between container rebuilds and restarts.

The SQLite database and environment files are excluded from Git and from the Docker build context.
