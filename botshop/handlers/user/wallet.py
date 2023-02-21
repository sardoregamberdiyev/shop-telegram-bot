
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from filters import IsUser
from .menu import balance

# test card ==> 1111 1111 1111 1026, 12/22, CVC 000

# shopId 506751

# shopArticleId 538350


@dp.message_handler(IsUser(), text=balance)
async def process_balance(message: Message, state: FSMContext):
    await message.answer("Elektron hamyon mavjud emas ❗\nYetqazib berishdan oldin kartaga 50% \n50% manzilga "
                         "yetqazib berilgandan so‘ng to‘lanadi 😉.\n/menu da Katolog bo'limida tavarni tanlashingiz "
                         "mumkin.")

