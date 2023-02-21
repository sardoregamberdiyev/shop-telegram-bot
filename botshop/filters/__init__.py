from aiogram import Dispatcher
from .is_admin import IsAdmin
from .is_user import IsUser

def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsAdmin, event_handlers=[dp.message_handlers])
    dp.filters_factory.bind(IsUser, event_handlers=[dp.message_handlers])
