from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_start_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Рассчет стоимости товара", callback_data="count_cost")],
        [InlineKeyboardButton(text="Попуск", url="https://t.me/voven0_0swoosh")],
        [InlineKeyboardButton(text="Отзывы", url="https://t.me/swoo_shop2")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard