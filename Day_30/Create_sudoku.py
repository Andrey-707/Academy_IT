# Программа Create_sudoku.py

# Программа создает из текстового файла 'ALL_SUDOKU.txt' размером 95 строк по 81 символ в каждой строке
# отдельные файлы 'puzzle+file_number.txt' для решения различных SUDOKU.

def create_sudoku(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = ''.join(f.read().split('\n'))

    number_of_files = len(data)//81

    step = 0
    for i in range(len(data)):
        if i % 9 ==0 and i !=0:
            data = data[:i+step] + '\n' + data[i+step:]
            step += 1 # с каждый добавленным символом перевода строки добавляем к шагу среза по единице

    k = 90
    for i in range(number_of_files):
        if i < 9:
            file_name = "All_SUDOKU\\" + "puzzle0" + str(i+1) + ".txt"
        else:
            file_name = "All_SUDOKU\\" + "puzzle" + str(i+1) + ".txt"
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(data[:k])
            data = data[k:]


# run
if __name__ == '__main__':
    create_sudoku('ALL_SUDOKU.txt')
