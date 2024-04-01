from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_end_kb():
    buttons = [
        [InlineKeyboardButton(text="Рассчитать цену снова", callback_data="count_cost")],
        [InlineKeyboardButton(text="Меню", callback_data="menu")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return(keyboard)