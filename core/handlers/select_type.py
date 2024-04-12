from aiogram import Router
from aiogram import F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import StateFilter
from ..keyboards.clothes import get_clothes_kb
from aiogram.fsm.context import FSMContext
from ..utils.statesform import StepsForm
from ..utils.weight import clothes, profit
from ..utils.get_cost import get_final_cost
from ..keyboards.end_kb import get_end_kb


router = Router()

@router.callback_query(F.data == "count_cost")
async def count_cost(callback: CallbackQuery, state: FSMContext):
    image = FSInputFile("core/media/photo_2023-03-21_09-53-31.jpg")
    await callback.message.answer_photo(image, caption='Для расчета всегда надо использовать перечеркнутую цену!!!')
    await callback.message.answer('Введите цену в юанях \n\n❗️Укажите целое число, без дробей, пробелов, букв и знаков валюты. Пример: 1250')
    await state.set_state(StepsForm.GET_COST)

@router.message(StepsForm.GET_COST, F.text.isdigit())
async def get_ya_cost(message: Message, state: FSMContext):
    await state.update_data(cost = int(message.text))
    await message.answer("Выберите тип товара", reply_markup=get_clothes_kb(list(clothes.keys())))
    await state.set_state(StepsForm.GET_TYPE)
    
@router.message(StepsForm.GET_COST, F.text)
async def incorrect_input(message: Message):
    await message.answer("incorrect input. Try again")


@router.callback_query(StepsForm.GET_TYPE)
async def get_type(callback:CallbackQuery, state:FSMContext):
    await state.update_data(type = callback.data)
    await callback.message.answer(f"Выберите размер", reply_markup=get_clothes_kb(list(clothes[callback.data])))
    await state.set_state(StepsForm.GET_SIZE)
    
@router.callback_query(StepsForm.GET_SIZE)
async def get_size(callback:CallbackQuery, state: FSMContext):
    await state.update_data(size = callback.data)
    user_data = await state.get_data()
    print(user_data)
    cost_item = user_data['cost']
    type = user_data['type']
    size = user_data['size']
    weight_cost = clothes[type][size]
    #рассчитать стоимость используя вес в юанях
    profit_vov = profit[type]
    final_cost = get_final_cost(cost_item, weight_cost, profit_vov)
    await state.clear()
    await callback.message.answer(f"Итоговая цена: {final_cost} BYN")
    
