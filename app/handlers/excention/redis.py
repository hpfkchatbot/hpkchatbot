from loguru import logger

import aiogram
from aiogram import types
from aiogram.filters import ExceptionTypeFilter
from redis import exceptions

from routers.excention import router


@router.errors(ExceptionTypeFilter(exceptions.ConnectionError))
async def redis_exceptions_connection(update: types.Update, file_exception, exception, bot: aiogram.Bot):
    logger.error(file_exception)
    logger.error(exception)
    message_text = 'Сталася помилка. С пробуй пізніше'
    await bot.send_message(text=message_text, chat_id=update.message.chat.id)
