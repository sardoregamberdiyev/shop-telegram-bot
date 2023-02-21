from aiogram.dispatcher.filters.state import StatesGroup, State


class SosState(StatesGroup):
    question = State()
    submit = State()


class AnswerState(StatesGroup):
    answer = State()
    submit = State()
