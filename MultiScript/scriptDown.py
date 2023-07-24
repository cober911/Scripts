# import time
# import click
import json
import re
import requests
from bs4 import BeautifulSoup
import browser_cookie3


link = "https://eva.finmarket.online/marketplace/sales/tinkoff_credit_card_full/get/"
file_path = "oxt.txt"
result_list = []
def process_link(link, file_path):  
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            result_list.append(link+line)
    return result_list
process_link(link, file_path)
# print("\n".join(result_list))


def filter_digits(input_string):
    return ''.join(char for char in input_string if char.isdigit())
spisok_download = []
def parser(url):
    # Подцепляет куки с браузера. Необходимо в браузере на пк залогинится. Следовательно сессия обновляется каждые 30 мин.
    cj = browser_cookie3.chrome()
    response = requests.get(url, cookies=cj)
    # Проверяем успешность запроса
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        # print(soup.prettify())
        script_tags = soup.find_all("script")
        # Проходим по всем скриптам и ищем тот, который содержит "let DATA"
        data_script = None
        for script_tag in script_tags:
            if "let DATA" in script_tag.text:
                data_script = script_tag.text
                break
        if data_script:
            # Используем регулярное выражение для извлечения JSON-строки из скрипта
            pattern = r"let\s+DATA\s*=\s*(\{.*\});"
            match = re.search(pattern, data_script)
            if match:
                data_json = match.group(1)
                try:
                    # Преобразуем JSON в словарь Python
                    data_dict = json.loads(data_json)
                    spisok_download.append("\n---------------   " + url +"    ---------------\n")
                    
                    keys_with_comments = {
                        "passport_main": "Основная страница паспорта",
                        "passport_registration": "Регистрация паспорта",
                        "consent": "Согласие на обработку",
                        "signed_consent": "Подписанное согласие",
                        "anketa": "Скан подписанных заявление-анкеты и заявки",
                        "card_photo": "Фото клиента с конвертом "
                    }
                    for key, comment in keys_with_comments.items():
                        try:
                            value = data_dict[key]
                            spisok_download.append(f"{comment}: https://eva.finmarket.online/media/download/{filter_digits(str(value))}")
                        except KeyError:
                            print(f"Ключ '{key}' не найден в словаре data_dict.")
                    
                except json.JSONDecodeError:
                    print("Ошибка декодирования JSON-строки.")
            else:
                print("Объект 'let DATA' не найден на странице1.")
        else:
            print("Объект 'let DATA' не найден на странице2.")
    else:
        print(f"Ошибка запроса. Код ответа: {response.status_code}")
        # time.sleep(5)

def process_urls_list(url_list):
    for url in url_list:
        parser(url)
process_urls_list(result_list)
print("\n".join(spisok_download))
# click.pause('Чтобы продолжить, нажмите Enter.')