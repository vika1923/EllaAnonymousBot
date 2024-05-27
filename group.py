import re

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from chat_types_filter import ChatTypeFilter
from dependencies import bot, specialists_chat_id
from db_manager import get_user_by_question

group_router = Router()
group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))

@group_router.message(Command('start'))
async def start_command_handler(message: Message) -> None:
    await message.answer("Welcome to specialists group!")


@group_router.message()
async def check_if_reply(message: Message):
    if message.reply_to_message:
        try:
            msg = message.reply_to_message
            user_id = get_user_by_question(extract_question_id(msg))
            await bot.send_message(chat_id=user_id,text="Your question was answered!")
            await bot.forward_message(chat_id=user_id, from_chat_id=specialists_chat_id, message_id=msg.message_id)
            await bot.forward_message(chat_id=user_id, from_chat_id=specialists_chat_id, message_id=message.message_id)
            await message.reply("Thank you for your answer!")

        except Exception as e:
            print("Error occurred while processing the reply message", e)


def extract_question_id(message: Message):
    print("extract_question_id")
    hashtag_pattern = r'#question(\d+)'
    if message.text:
        match = re.search(hashtag_pattern, message.text)
        if match:
            return match.group(1)
    elif message.caption:
        match = re.search(hashtag_pattern, message.caption)
        if match:
            return match.group(1)

