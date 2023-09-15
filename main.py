import logging
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from buttons import get_region_change, get_region_kb
import requests
import json


API_TOKEN ='6569387811:AAECcUzgYtZ1ixCbrI4feq8hqNQR5SaCw60'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Form_weather(StatesGroup):
    started_state = State()
    region_choice_state = State()
    region_shows_state = State()
    
reply_markup = get_region_change()
reply_markup_json = json.dumps(reply_markup.to_python())
region_change_markup = types.InlineKeyboardMarkup()
new_region_markup = types.InlineKeyboardMarkup()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет, выбери город, в котором хочешь узнать погоду🌡🌈', reply_markup= get_region_change())
    await Form_weather.started_state.set()
    

@dp.callback_query_handler(state=Form_weather.started_state)
async def region_choice(query: types.CallbackQuery, state: FSMContext):
    
    if query.data == 'Меню выбора':
        
        # time.sleep(0.3)
        await query.message.edit_text('Вот список доступных регионов 📃', reply_markup=get_region_kb())
        await Form_weather.region_shows_state.set()
    
@dp.callback_query_handler(state=Form_weather.region_shows_state)
async def change(query: types.CallbackQuery, state: FSMContext):
    
    if query.data != 'Меню выбора':
        Region = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={query.data}&appid=9481a85b5698cd4123700515f65695b7').json()
        

        temp = str(round(Region['main']['temp'] - 273)) + ' ℃'
        humidity = str(Region['main']['humidity']) + ' %'
        wind = str(round((Region['wind']['speed']) * 1.6)) + ' Км/ч'
        clouds = str(Region['clouds']['all']) + ' %'

        region_name = {
            'Odessa': 'в Одессе',
            'Kyiv': 'в Киеве',
            'Kharkov': 'в Харькове',
            'Lviv': 'во Львове',
            'Poltava': 'в Полтаве',
            'Dnipro': 'в Днепре',
            'Cherkasy': 'в Черкассах',
            'Zaporizhzhia': 'в Запорожье',
            'Mykolaiv': 'в Николаеве',
            'Kherson': 'в Херсоне',
            'Uzhhorod': 'в Ужгороде',
            'Chernihiv': 'в Чернигове',
            'Sumy': 'в Сумах',
            'Uman': 'в Умани',
            'Ternopil': 'в Тернополе',
        }

        await query.message.edit_text(
    f'Погода {region_name[query.data]}:\nТемпература🌡: {temp}\nВлажность💧: {humidity}\nСкорость ветра🌬: {wind}\nОблачность☁: {clouds}',
    reply_markup=reply_markup_json
)
    else:   
        time.sleep(0.2)
        await query.message.edit_text('Меню выбора 🌏  ', reply_markup=get_region_kb())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
