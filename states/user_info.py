from telebot.handler_backends import State, StatesGroup


class Info(StatesGroup):
    city = State()
    hotels_limit = State()

    check_in = State()
    check_out = State()

    req_photo = State()
    photo_limit = State()