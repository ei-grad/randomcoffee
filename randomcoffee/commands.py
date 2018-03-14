def welcome_message(req):
    return {
        'method': 'sendMessage',
        'chat_id': req['chat']['id'],
        'text': '''Добро пожаловать на #randomcoffee!
Для начала укажите свой город и выберите как часто вы хотите получать приглашения:
'''
    }


def city_keyboard(req):
    return {}


commands = {
    '/start': welcome_message,
    '/city': city_keyboard,
}
