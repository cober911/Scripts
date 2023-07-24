# Разница в скорости между двух запросов Редаш по результату 100 запросов

import os
import requests
import time
from statistics import mean
import json

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

def poll_job(s, redash_url, job):
    # TODO: add timeout
    while job['status'] not in (3, 4):
        response = s.get('{}/api/jobs/{}'.format(redash_url, job['id']))
        job = response.json()['job']
        time.sleep(1)

    if job['status'] == 3:
        return job['query_result_id']

    return None


def get_fresh_query_result(redash_url, query_id, api_key, params):
    s = requests.Session()
    s.headers.update({'Authorization': 'Key {}'.format(api_key)})

    payload = dict(max_age=0, parameters=params)

    response = s.post('{}/api/queries/{}/results'.format(redash_url, query_id), data=json.dumps(payload))

    if response.status_code != 200:
        raise Exception('Refresh failed.')

    result_id = poll_job(s, redash_url, response.json()['job'])

    if result_id:
        response2 = s.get('{}/api/queries/{}/results/{}.json'.format(redash_url, query_id, result_id))
        if response.status_code != 200:
            raise Exception('Failed getting results.')
    else:
        raise Exception('Query execution failed.')

    return response2.json()['query_result']['runtime']


if __name__ == '__main__':
    api_key = '' # !!! отсюда https://redash-d.finfort.ru/users/me
    query1_id = 233
    params1 = {'contexts': ['Select All'],
              'divisions': ['Select All'],
              'orgnames': ['Select All'],
              'date': {
                  'start': '2022-06-01',
                  'end': '2023-06-14'}
              }
    query2_id = 229
    params2 = {'contexts': ['Select All'],
              'divisions': ['Select All'],
              'orgnames': ['Select All'],
              'date': {
                  'start': '2022-06-01',
                  'end': '2023-06-14'},  # !!! ↓ Заменить все %ХХ ↓
              'reestr': 'Халва полный цикл^ID заявки$|^Доставка/Лид$|^Легаси/УЗ$|^Алиас$|^Оффер$|^ID клиента$|^ФИО клиента$|^Дата рождения$|^Мобильный телефон$|^Статус заявки сырой$|^УЗ - Текущее состояние$|^УЗ - ID заявки (внешний)$|^УЗ - Нормализованный статус$|^Статус модерации$|^Синтетический статус F0$|^Синтетический статус F1$|^Синтетический статус F2$|^Статус по проверке фото$|^Статус по звонку$|^Комментарий$|^Продажи$|^ID Подразделения$|^Подразделение$|^Контекст подразделения$|^Организация$|^ID Организации$|^Создатель$|^UTM Medium$|^UTM Term$|^ID Создателя$|^Дата создания$|^Месяц создания заявки$|^Время создания заявки$|^Номер карты$|^Город$|^Регион$|^ГЕО id$|^Сквозной идентификатор$|^Код ТТ$|^Срок жизни заявки$|^Убер$|^Единый статус$|^Тип продукта$|^Местонахождение заявки$'
              }
    answer1 = []
    answer2 = []
    count = 100
    printProgressBar(0, count, prefix='Отправлено:', suffix='запросов', length=50)
    for i in range(count):
        printProgressBar(i, count, prefix='Отправлено:', suffix='запросов', length=50)
        answer1.append(get_fresh_query_result('https://redash-d.finfort.ru', query1_id, api_key, params1))
        answer2.append(get_fresh_query_result('https://redash-d.finfort.ru', query2_id, api_key, params2))
        time.sleep(3)
    print('\nСреднее арифметическое по ', count, ' запросам:\n  - без фильтрации ' , mean(answer1),
          '\n  - с фильтрацией ', mean(answer2))

