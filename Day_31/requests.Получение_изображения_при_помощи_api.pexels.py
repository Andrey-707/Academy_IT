# Получение изображения при помощи API

import requests

from rich import print


def download(q, p):
    """
    Функция получает изображение с сайта https://pexels.com при помощи api.
    """
    header = {"Authorization": "563492ad6f917000010000015478534fd69f4e74b36153a06c31849f"}

    for i in range(1, 5+1):
        url = f"https://api.pexels.com/v1/search?query={q}&per_page=1&page={i}"

        r = requests.get(url, headers=header)

        if r.status_code == 200:
            _r = r.json()
            print(f"Номер: {i}")
            print(_r.get("photos")[0].get("src").get("medium")) # выдет URL, для просмотра фото скопировать в браузер
            print(_r.get("photos")[0].get("photographer"))
            print(_r.get("photos")[0].get("alt"))
        else:
            print(r.status_code)

def main():
    """
    Главная функция. Получает тематику изображения от пользователя, затем получает изображение.
    """
    # q = input("Тематика фото: ")
    q = "cat"
    download(q, 5)


# run
if __name__ == '__main__':
    main()
