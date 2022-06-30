# Решение SUDOKU в чате Telegram бота. Telegram_Bot.Sudoku_1.0
# Sudoku_1bot
# Sudoku_Bot

# Программа возвращает в чат Telegram решенную головоломку SUDOKU если пользователь нажмет кнопку с
# надписью '🎲 Solve It'. Пустой символ представлен в виде нолика.

import telebot, pathlib

from rich import print
from telebot import types
from sudoku_config import token


bot = telebot.TeleBot(token)


def read_sudoku(path):
    """
    Принимает путь (файл .txt), открывает файл на чтение.
    Возвращает данные из файла в виде двумерного массива.
    """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    digits = [c for c in puzzle if c in '1234567890']
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


def solve():
    """
    Функция решения SUDOKU.
    """
    global gmap, vmap
    for y in range(9):
        for x in range(9):
            if gmap[y][x] == '0':
                for n in range(1, 10):
                    number = str(n)
                    if possible(gmap, y, x, number):
                        gmap[y][x] = number
                        solve()
                        gmap[y][x] = '0'
                return
    vmap = visual_map(gmap)

def show_map(vmap):
    """
    Добавляет кнопку. Выводит данные в чат.
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Solve It")
    markup.add(item1)
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
    # message
    bot.send_message(message.chat.id,
    "Hi, {0.first_name}!\n"
    "I am <b>{1.first_name}</b>.\n".format(
        message.from_user, bot.get_me()), parse_mode='html')

    # visual map
    vmap = visual_map(gmap)

    # Message
    bot.send_message(message.chat.id, **show_map(vmap))


@bot.message_handler(content_types=["text"])
def send_messeges(message):
    if message.text == "🎲 Solve It":
        solve()
        bot.send_message(message.chat.id, **show_map(vmap))


# Handle pressing buttons
@bot.callback_query_handler(func=lambda call: True)
def echo_message(call):
    """
    Callback function.
    """
    bot.reply_to(call.message, call.data)


print("Program start")

# Game Map
gmap = read_sudoku('Telegram_Sudoku1.txt')
print(gmap)

bot.polling(none_stop=True)

print("Program finish")
