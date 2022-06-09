import config
import logging
import random
from aiogram import Bot, Dispatcher, executor, types

# from aiogram.types import ContentType, Message

''' 1.Управляемый иди нахуй, 2.Добавить анекдоты'''

# log
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)

lst = ['России', 'россии', 'росия', 'россия', 'Россия', 'Россию', "россию"]
lst1 = ["Украина", "Україна", "україна", "украина", "слава украине", "Украине", "Слава Україні"]
lst2 = ['Героям Слава', "героям слава", "Героям слава"]
Putin = "Путин", "путин", "пыня", "Пыня"

animation_id = 'AgACAgIAAx0CT-J_lAAD_mKJrXsvOE5A_XBCiTGgdGiNo76LAAJ6vDEbLAJQSGiPH1W4a156AQADAgADbQADJAQ'
animation_id1 = 'CgACAgIAAx0CT-J_lAADdWKIwJ14vGQ2uYzwdQABNNJ_o4cTpwACXRQAAttOYUkGWiOC2QABxIUkBA'
grace_voice_id = 'AwACAgIAAx0CT-J_lAACAadiiiNcWMoYz2bcaM4vy6IYzZ4bhQACMRsAAiwCUEhcEFqg2vjWNSQE'
grace_photo_id = 'AgACAgIAAx0CT-J_lAACAfViii1RBR_KO_7I1jQFquT_3YkExAACA74xGywCUEi39vmYE--8QAEAAwIAA20AAyQE'
exorcism_id = 'AwACAgIAAxkBAAIBFGKLc3CP_2zHkLLZ0CZuAs8lGGP6AALGGQACjYhhSMHpb17uAAH4dCQE'
exorcism_animation_id = 'CgACAgQAAxkBAAIBImKLdIk7eiuQ5n8WQwUpqeUVYE-bAAL-AgACmJ0MUw0ndYhIkiMdJAQ'
scream_voice_id = 'AwACAgIAAxkBAAPLYotskvdnCRaayAWmTbl90BkPltcAAtYcAAIjfVlIJIhDaf9eMcAkBA'
scream_animation_id = 'CgACAgQAAxkBAAIBR2KLdkNUE-ZDXcJcUbUTWv8asrd6AAJZAwACAVgEU_UU4U7jIs_HJAQ'
masha_voice_id = 'AwACAgIAAxkBAAIBnGKLetvi6uzT8SF9nwjcoino-NBwAALxGQACjYhhSCnK3cebfj3GJAQ'
putin_dick_id = 'AgACAgIAAxkBAAIES2KTMyEVd-3w-rFVFVQhIGRHFGVGAALWujEbs8mYSMqu9I46pulqAQADAgADbQADJAQ'
die_for_enemies = 'AgACAgIAAxkBAAIEc2KTN1ekKkpTPHcmgBetwugZ3DesAALYujEbs8mYSJJ8ztA8LzhEAQADAgADbQADJAQ'


# @dp.message_handler(content_types=ContentType.PHOTO)
# async def send_photo_file_id(message: Message):
# await message.reply(message.photo[-1].file_id)

# фильтр

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("Рандомное число /random \nМолитва /grace \nОбряд /exorcism \nКрик /scream \
    \nЦитата дня /quotes \nТемы для общения /themes \nКомлимент /compliment")


@dp.message_handler()
async def filter_messages(message: types.Message):
    if '/random' in message.text:
        await message.answer(str(random.randint(0, 100)))

    if '/exorcism' in message.text:
        await message.reply("Обряд изгнанания начат")
        await dp.bot.send_voice(chat_id=message.chat.id, voice=exorcism_id)
        await dp.bot.send_animation(chat_id=message.chat.id, animation=exorcism_animation_id)

    elif '/grace' in message.text:
        await message.reply("Амінь!")
        await dp.bot.send_voice(chat_id=message.chat.id, voice=grace_voice_id)
        await dp.bot.send_photo(chat_id=message.chat.id, photo=grace_photo_id)

    elif '/quotes' in message.text:
        await message.answer(random.choice(list(open('quotes2.txt', encoding="utf-8"))))

    elif '/compliment' in message.text:
        await message.answer(random.choice(list(open('compliment.txt', encoding="utf-8"))))

    elif '/themes' in message.text:
        await message.answer(random.choice(list(open('themes.txt', encoding="utf-8"))))

    elif '/scream' in message.text:
        await dp.bot.send_voice(chat_id=message.chat.id, voice=scream_voice_id)
        await dp.bot.send_animation(chat_id=message.chat.id, animation=scream_animation_id)

    elif 'иди на хуй' in message.text:
        await dp.bot.send_voice(chat_id=message.chat.id, voice=masha_voice_id,
                                reply_to_message_id=message.message_id)

    for p in Putin:
        if p in message.text:
            await dp.bot.send_photo(chat_id=message.chat.id, photo=putin_dick_id,
                                    reply_to_message_id=message.message_id)
    # гачи украина русня
    for i in lst:
        if i in message.text:
            await dp.bot.send_animation(chat_id=message.chat.id, animation=animation_id1,
                                        reply_to_message_id=message.message_id)

    # стикер ниги с зигой
    for j in lst1:
        if j in message.text:
            await dp.bot.send_photo(chat_id=message.chat.id, photo=animation_id, reply_to_message_id=message.message_id)

    # стикер резать
    for k in lst2:
        if k in message.text:
            await message.reply("Смерть ворогам!")  # стикер резать
            await dp.bot.send_photo(chat_id=message.chat.id, photo=die_for_enemies)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
