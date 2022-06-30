# -*- coding: utf-8 -*-
# Решение SUDOKU в чате Telegram бота. Telegram_Bot.Sudoku
# Sudoku_1bot
# Sudoku_Bot

# Программа с интервалом в 1 секунду меняет в чате Telegram каждый символ нерешенной головоломки
# SUDOKU на подходящий символ если пользователь нажмет кнопку с надписью '🎲 Solve It'.
# Стартовое поле запускается командой '/start' или '/help', отправленной в чат Telegram.
# Пустой символ представлен в виде точки.

# 😺 😺 😺
# НЕ смотря на паузу при отправке сообщений в 1 секунду подобный способ работы с Telegram ботом
# приводит к систематическим ошибкам:
# Error code: 429. Description: Too Many Requests: retry after ...

import telebot, pathlib, time

from telebot import types
from sudoku_config import token
from rich import print


bot = telebot.TeleBot(token)


def read_sudoku(path):
    """
    Принимает путь (файл .txt), открывает файл на чтение.
    Возвращает данные из файла (сетку или список списков).
    """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    digits = [c for c in puzzle if c in '123456789.']
    grid = [digits[9*i: 9*i+9] for i in range(9)]
    return grid


def visual_map(A):
    """
    Принимает сетку SUDOKU, выводит отформатировнную сетку на экран.
    """
    text = ""
    for i in range(9):
        if i % 3 == 0:
            if i == 0:
                text += "┎─────────────────────────┒\n"
            else:
                text += "┠─────────────────────────┨\n"
        for j in range(9):
            if j % 3 == 0:
                text += "┃ "
            if j == 8:
                text = text + str(A[i][j]) + " ┃ "
            else:
                text = text + str(A[i][j]) + " "
        text += "\n"
    text += "┖─────────────────────────┚"
    return text


def possible(grid, y, x, n):
    """
    Функция проверяет, может ли число находиться в определенной ячейке SUDOKU.
    Принимает сетку, координаты числа и число. Возвращает логическое значение.
    """
    numbers = [str(i) for i in range(1, 10)]
    if n not in numbers:
        return False

    for i in range(9):
        if grid[y][i] == n:
            return False

    for i in range(9):
        if grid[i][x] == n:
            return False

    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
    return True


def show_map(vmap):
    """
    Add button. Data output to chat.
    """
    btn = types.InlineKeyboardButton
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(btn("🎲 Solve It", callback_data="0"))
    return {
        'text': '<code>' + vmap + '</code>',
        'reply_markup': markup,
        'parse_mode': 'html'
    }


# Handle '/start' and '/help'
@bot.message_handler(commands=['start', 'help'])
def welcome_and_map(message):
    """
    Reply to user message '/start' or '/help'. Add map.
    """
    global vmap

    # message
    bot.send_message(message.chat.id,
    "Hi, {0.first_name}!\n"
    "I am <b>{1.first_name}</b>.\n".format(
        message.from_user, bot.get_me()), parse_mode='html')

    # visual map
    vmap = visual_map(gmap)

    # send map in chat
    bot.send_message(message.chat.id, **show_map(vmap))


def replace_on_map(game_map, pos, char):
    """
    Function makes replacements on the map.
    """
    return game_map[:pos] + char + game_map[pos+1:]


# Handle pressing buttons
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    """
    Callback function.
    """
    def solve(gmap):
        """
        Функция решения SUDOKU.
        """
        global vmap
        for y in range(9):
            for x in range(9):
                if gmap[y][x] == '.':
                    for n in range(1, 10):
                        number = str(n)
                        if possible(gmap, y, x, number):
                            gmap[y][x] = number
                            solve(gmap)
                            gmap[y][x] = '.'
                    return

        for i, row in enumerate(gmap):
            for j, sym in enumerate(row):
                pos = vmap.find('.')
                if read_sudoku(file)[i][j] not in '123456789' and pos != len(vmap)-1:
                    vmap = replace_on_map(vmap, pos, sym)
                    bot.edit_message_text(
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        **show_map(vmap)
                        )
                    time.sleep(1)

    try:
        # solve SUDOKU
        solve(gmap)

        # check result
        if vmap.count(u'.') == 0:
            bot.send_message(call.message.chat.id, "Поздравляю! Вы выиграли!")

    except IndexError as IE:
        print(repr(IE))


# run
if __name__ == '__main__':
    file = 'Telegram_Sudoku2.txt'
    gmap = read_sudoku(file)
    bot.polling(none_stop=True)
