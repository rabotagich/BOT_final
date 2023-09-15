from aiogram import types


def get_region_change():
    region_change_markup = types.InlineKeyboardMarkup()
    region_change_markup.add(types.InlineKeyboardButton('Меню выбора🤗', callback_data='Меню выбора'))
    return region_change_markup

def get_region_kb():
    region_kb = types.InlineKeyboardMarkup()
    region_kb.add(
        types.InlineKeyboardButton('Одесса', callback_data='Odessa'),
        types.InlineKeyboardButton('Киев', callback_data='Kyiv'),
        types.InlineKeyboardButton('Харьков', callback_data='Kharkov'),
        types.InlineKeyboardButton('Львов', callback_data='Lviv'),
        types.InlineKeyboardButton('Полтава', callback_data='Poltava'),
        types.InlineKeyboardButton('Днепр', callback_data='Dnipro'),
        types.InlineKeyboardButton('Черкассы', callback_data='Cherkasy'),
        types.InlineKeyboardButton('Запорожье', callback_data='Zaporizhzhia'),
        types.InlineKeyboardButton('Николаев', callback_data='Mykolaiv'),
        types.InlineKeyboardButton('Херсон', callback_data='Kherson'),
        types.InlineKeyboardButton('Ужгород', callback_data='Uzhhorod'),
        types.InlineKeyboardButton('Чернигов', callback_data='Chernihiv'),
        types.InlineKeyboardButton('Суми', callback_data='Sumy'),
        types.InlineKeyboardButton('Умань', callback_data='Uman'),
        types.InlineKeyboardButton('Тернополь', callback_data='Ternopil'),
    )
    return region_kb




