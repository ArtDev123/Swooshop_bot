from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# def get_clothes_keyboard():
#     buttons = [
#         [InlineKeyboardButton(text="Кроссовки", callback_data="sneakers")],
#         [InlineKeyboardButton(text="Ботинки", callback_data="shoes")],
#         [InlineKeyboardButton(text="Футболки, аксессуары, гол. уборы", callback_data="t_shorts")],
#         [InlineKeyboardButton(text="Шорты", callback_data="shorts")],
#         [InlineKeyboardButton(text="Худи, толстовки, штаны", callback_data="hudy")],
#         [InlineKeyboardButton(text="Пуховики, жилетки", callback_data="puh")],
#         [InlineKeyboardButton(text="Сумки, рюкзаки", callback_data="bags")],
#         [InlineKeyboardButton(text="Начать сначала", callback_data="count_cost")],
#         [InlineKeyboardButton(text="Меню", callback_data="menu")]
#     ]

#     keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
#     return keyboard

def get_clothes_kb(btns):
    buttons = []
    for btn in btns:
        buttons.append([InlineKeyboardButton(text=btn, callback_data=btn)])
    buttons.append([InlineKeyboardButton(text="Начать сначала", callback_data="count_cost")])
    buttons.append([InlineKeyboardButton(text="Меню", callback_data="menu")])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard
    
    
