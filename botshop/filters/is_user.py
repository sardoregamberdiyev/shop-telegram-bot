from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter
from data.config import ADMINS


class IsUser(BoundFilter):

    async def check(self, message: Message):
        return message.from_user.id not in ADMINS
