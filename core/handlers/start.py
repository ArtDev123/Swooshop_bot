from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from core.keyboards.start_kb import get_start_keyboard

router = Router()

@router.message(Command("start"))
async def get_start(message: Message):
    await message.answer(f"Привет! Вы запустили бота SWOO._.SHOP \n Канал: t.me/swoo_shop")
    await message.answer("Выберите нужное действие:", reply_markup=get_start_keyboard())
