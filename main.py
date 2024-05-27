import asyncio
from dependencies import dp
from private import private_router
from group import group_router
from db_manager import start_db, clear_table

dp.include_router(private_router)
dp.include_router(group_router)

async def main() -> None:
    from dependencies import bot
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    start_db()
    asyncio.run(main())
    
