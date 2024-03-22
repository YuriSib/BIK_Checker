import time
import telebot


bot = telebot.TeleBot('6419841809:AAFEiToc-LKefUbh7nkzEiusYGnHgA0NAK8')


@bot.message_handler(commands=['start'])
def test(message_):
    chat_id = message_.chat.id
    bot.reply_to(message_, f"Your chat ID is: {chat_id}")


def start_iteration(qantity_districts, districts):
    bot.send_message(
        674796107,
        f'Итерация запущена. На данный момент в БИКе {qantity_districts} районов: {districts}. '
        f'Перейти на сайт: https://cabinet.bik31.ru/map?type=RESIDENTIAL_PLOTS'
    )
    bot.send_message(
        383905997,
        f'Итерация запущена. На данный момент в БИКе {qantity_districts} районов: {districts}. '
        f'Перейти на сайт: https://cabinet.bik31.ru/map?type=RESIDENTIAL_PLOTS'
    )


def message(district):
    bot.send_message(674796107, f'В БИКе добавлен {district} для покупки участков!\n '
                                f'Перейти на сайт: https://cabinet.bik31.ru/map?type=RESIDENTIAL_PLOTS')
    bot.send_message(383905997, f'В БИКе добавлен {district} для покупки участков!\n '
                                f'Перейти на сайт: https://cabinet.bik31.ru/map?type=RESIDENTIAL_PLOTS')


def reduction_list_message(district):
    bot.send_message(674796107, f'Все участки в {district} раскуплены!\n '
                                f'Перейти на сайт: https://cabinet.bik31.ru/map?type=RESIDENTIAL_PLOTS')
    bot.send_message(383905997, f'Все участки в {district} раскуплены!\n '
                                f'Перейти на сайт: https://cabinet.bik31.ru/map?type=RESIDENTIAL_PLOTS')


def list_oskol_districts(districts):
    bot.send_message(674796107, f'На текущий момент в Старооскольском ГО имеются  следующие микрорайоны : {districts}\n'
                                f'Перейти на сайт: https://cabinet.bik31.ru/map?type=RESIDENTIAL_PLOTS&municipality=29')
    bot.send_message(383905997, f'На текущий момент в Старооскольском ГО имеются  следующие микрорайоны : {districts}\n'
                                f'Перейти на сайт: https://cabinet.bik31.ru/map?type=RESIDENTIAL_PLOTS&municipality=29')


def oskol_new_district(district):
    bot.send_message(674796107, f'В Старооскольском ГО появился новый микрорайон: {district}!\n '
                                f'Перейти на сайт: https://cabinet.bik31.ru/map?type=RESIDENTIAL_PLOTS&municipality=29')
    bot.send_message(383905997, f'В Старооскольском ГО появился новый микрорайон: {district}!\n '
                                f'Перейти на сайт: https://cabinet.bik31.ru/map?type=RESIDENTIAL_PLOTS&municipality=29')


def oskol_del_district(district):
    bot.send_message(674796107, f'В Старооскольском ГО куплен участок: {district}!\n '
                                f'Перейти на сайт: https://cabinet.bik31.ru/map?type=RESIDENTIAL_PLOTS&municipality=29')
    bot.send_message(383905997, f'В Старооскольском ГО куплен участок: {district}!\n '
                                f'Перейти на сайт: https://cabinet.bik31.ru/map?type=RESIDENTIAL_PLOTS&municipality=29')


def get_status_400():
    bot.send_message(674796107, f'Ошибка! Ответ на get-запрос пришел со статусом, отличным от 200!')
    bot.send_message(383905997, f'Ошибка! Ответ на get-запрос пришел со статусом, отличным от 200!')


def error_message(e):
    bot.send_message(674796107, f'В работе кола возникла ошибка {e}')