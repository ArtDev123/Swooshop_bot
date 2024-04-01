from aiogram.fsm.state import StatesGroup, State

class StepsForm(StatesGroup):
    GET_COST = State()
    GET_COST_KB = State()
    GET_TYPE = State()
    GET_SIZE = State()
