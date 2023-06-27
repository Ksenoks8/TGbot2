import telebot
from telebot.types import ReplyKeyboardMarkup,KeyboardButton,Message
from .datab import Database
from random import choice
class Bot(telebot.TeleBot):
    def __init__ (self,token):
        super().__init__(token)
        self.stickers = {'random-stickers':[
            'CAACAgIAAxkBAAIf22SVaTksrl4breYqscPPImpQfu7uAAKeAAPBnGAM3ba7tFYuCMkvBA',
            'CAACAgIAAxkBAAIfwGSVaP9pEp0o3WMtaUY_Fi7sl9dFAAIxAQACUomRI3LvjO7IVGFzLwQ',
            'CAACAgIAAxkBAAIft2SVaORsIaNa6l9GXwnyfGb-rmILAAKJCgACcW6JS9OXXOiMKwOwLwQ',
            'CAACAgIAAxkBAAIftGSVaNo-JRtyEwr8bKTQeZm93s6GAAISEgACTJHoSqI0uvk0kAnILwQ',
            'CAACAgIAAxkBAAIfrmSVaNNJ15UYI2SAtiNxL2a0LPOzAAI9AQACFkJrCtPHcKCCUMr-LwQ',
            'CAACAgIAAxkBAAIfqGSVaMR9MOzRTPrcBXgOVZvKMvv8AAIYAAPANk8T1vonv5xqGPgvBA',
            'CAACAgIAAxkBAAIfpWSVaLrbg-AtgRwnAujengNwmIUcAALNAQACFkJrCsvZm3sWgi-4LwQ'
            ],
            'kalkulator':['CAACAgIAAxkBAAIgfGSaqZLfbqYUbHBih_yh7y9J5Jq6AAJiAANOXNIpTqLDGEjEK3EvBA']}
        self.datab = Database('user.json')
        self.featuresMarkup=ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
        self.featuresMarkup.add(
            KeyboardButton('Взлом пентагона👨‍💻'),
            KeyboardButton('Калькулятор💻'),
            KeyboardButton('Рандомный стикер❓'),
            KeyboardButton('Игра 9 жизней🎰'),
            KeyboardButton('Искать видео🔎'),
            KeyboardButton('Инфа🛑')
        )
        self.OTMENA = ReplyKeyboardMarkup(resize_keyboard=True)
        self.OTMENA.add(KeyboardButton('Отмена❌'))
        
        self.register_message_handler(callback = self.on_start,commands = ['start'])
        self.register_message_handler(callback = self.on_info,commands = ['info'])
        self.register_message_handler(callback = self.on_other_message)

    def on_start(self,message:Message):
        userId = message.from_user.id
        if self.datab.user_exists(userId):
            name = message.from_user.full_name
            self.send_message(userId,'Hello, ' + name)
        else:
            self.datab.create_user(userId)
            self.send_message(userId,'Вас приветсвует бот!',reply_markup=self.featuresMarkup)
        self.send_sticker(userId,'CAACAgIAAxkBAAIfkGSVZYklV5w9PedJa3D-BlHRG083AAKOAQACK15TCzBEoy95j_E7LwQ')
        self.send_sticker(userId,'CAACAgIAAxkBAAIfmWSVZe_a501X7VEXKfD4VislE_HjAAKHAQACK15TC3gn1k2Gf2lgLwQ')
    def on_info(self,message:Message):
        userId = message.from_user.id
        self.send_message(userId,'Это мой первый бот,пока что он не доработан,но скоро будет многофункциональным',reply_markup=self.featuresMarkup)
        self.send_sticker(userId,'CAACAgIAAxkBAAIfd2SVYqmsiZWAQH2rvlHdj1BnZ05UAAL7CgACbzShSyxq7F1NG7V4LwQ')
        self.send_sticker(userId,'CAACAgIAAxkBAAIfjWSVZQHlwZPDYNHXRKEME2PBqUf7AAJcAANSiZEjVoQjitwpmnQvBA')
    def on_other_message(self,message:Message):
        userId = message.from_user.id
        userState = self.datab.get_user(userId)['state']
        if userState == 'kalkulator':
            self.OTMENA(userId,message.text)
        else:
            self.on_none_state(userId,message.text,message.from_user.first_name)
    def OTMENA(self,userId:int,text:str) -> None:
        if text == 'Отмена❌':
            markup = self.featuresMarkup
            message = 'Чем займемся теперь?'
            self.datab.update_user(userId,state = 'menu')
        


    def on_none_state(self,userId,text,name):
        if text == 'Взлом пентагона👨‍💻':
            pass
        elif text == 'Калькулятор💻':
            self.datab.update_user(userId,state = 'kalkulator')
            self.send_message(userId,'Напишите пример',reply_markup==self.OTMENA)
            self.send_sticker(userId,self.sticker= ['kalkulator'])
        elif text == 'Рандомный стикер❓':
            self.send_sticker(userId,choice(self.stickers['random-stickers']))
        elif text == 'Игра 9 жизней🎰':
            pass
        elif text == 'Искать видео🔎':
            pass
        elif text == 'Инфа🛑':
            pass
        else:
            self.send_message(userId,'Я не знаю такого действия!',reply_markup=self.featuresMarkup)

    