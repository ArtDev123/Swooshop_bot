from aiogram import Router, F
from aiogram.types import CallbackQuery
from ..keyboards.start_kb import get_start_keyboard

router = Router()

@router.callback_query(F.data == "menu")
async def go_to_menu(callback: CallbackQuery):
    await callback.message.answer("Выберите нужное действие", reply_markup=get_start_keyboard())