import asyncio

from aiogram import F, Router
from aiogram.filters import Command, or_f
from aiogram import types
from dependencies import bot, specialists_chat_id
from chat_types_filter import ChatTypeFilter

from db_manager import get_max_primary_key, add_to_waitlist

private_router = Router()
private_router.message.filter(ChatTypeFilter(["private"]))

@private_router.message(Command('start'))
async def start_command_handler(message: types.Message) -> None:
    await message.answer("Welcome to Ella Anonymous Bot! \nSend me your question and get the answer from a specialist.")

@private_router.message(F.text)
async def forward_to_group(message: types.Message):
    await bot.send_message(chat_id=specialists_chat_id, text=message.text + "\n\n#question" + str(get_max_primary_key() + 1))
    await asyncio.to_thread(add_to_waitlist, message.from_user.id)
    await message.answer("Your message was sent")


@private_router.message(F.photo)
async def forward_to_group_media(message: types.Message):
    caption = message.caption + "\n\n#question" + str(get_max_primary_key() + 1)
    await bot.send_photo(photo=message.photo[0].file_id, chat_id=specialists_chat_id, caption=caption)
    await asyncio.to_thread(add_to_waitlist, message.from_user.id)
    await message.answer("Your message was sent")

@private_router.message(F.video)
async def forward_to_group_media(message: types.Message):
    caption = message.caption + "\n\n#question" + str(get_max_primary_key() + 1)
    await bot.send_video(video=message.video.file_id, chat_id=specialists_chat_id, caption=caption)
    await asyncio.to_thread(add_to_waitlist, message.from_user.id)
    await message.answer("Your message was sent")