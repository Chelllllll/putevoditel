import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Объект бота
bot = Bot(token="6956350112:AAEI_7pkfRPk9toVv_z5SswtH9Y0xstuIDA")
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Москва"),
        types.KeyboardButton(text="Санкт-Петербург")
    )
    builder.row(types.KeyboardButton(text="Волгоград"),
                types.KeyboardButton(text="Воронеж"),
                types.KeyboardButton(text="Екатеринург")
                )
    builder.row(types.KeyboardButton(text="Казань"),
                types.KeyboardButton(text="Красноярск"),
                types.KeyboardButton(text="Краснодар")
                )
    builder.row(types.KeyboardButton(text="Нижний Новгород"),
                types.KeyboardButton(text="Новосибирск"),
                types.KeyboardButton(text="Омск")
                )
    builder.row(types.KeyboardButton(text="Пермь"),
                types.KeyboardButton(text="Ростов-на-Дону"),
                types.KeyboardButton(text="Самара")
                )
    builder.row(types.KeyboardButton(text="Челябинск"),
                types.KeyboardButton(text="Уфа")
                )
    await message.answer(f"""Привет, {message.from_user.first_name}! (๑'ᵕ'๑) 
✦ Я бот-путеводитель помогу тебе найти интересные места в крупных городах России! 
✦ Выбери город, который тебя интересует!""", reply_markup=builder.as_markup(resize_keyboard=True))


@dp.message()
async def condition(messege: types.Message):
    if messege.text == "Москва":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Санкт-Петербург":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Новосибирск":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Казань":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Екатеринург":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Нижний Новгород":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Красноярск":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Челябинск":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Самара":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Уфа":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Ростов-на-Дону":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Краснодар":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Омск":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Воронеж":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Пермь":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    elif messege.text == "Волгоград":
        await messege.answer("Здорово!", reply_markup=types.ReplyKeyboardRemove())
    else:
        await messege.answer("✦ Город указан не верно. Напишите правильное название...")


@dp.message(F.date)
async def cmd_places(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Активный отдых")
    )
    await message.answer("•⩊• Как вы планируете отдохнуть?"  # хочу поспать...
                         "Выберите нужный вариант:", reply_markup=builder.as_markup())


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
