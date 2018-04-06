import requests


curr_req = requests.get('https://api.hh.ru/dictionaries')
curr_list = curr_req.json().get('currency') # Список словарей валюты


#Получение курса валюты
def get_currency_rate(currency):
    for curr in curr_list:
        if curr.get('code') == currency:
            return curr.get('rate')


#Получение зарплаты из вилки
def get_avg_salary(low, high, currency):
    if low is None:
        avg_slr = high
    elif high is None:
        avg_slr = low
    else:
        avg_slr = (low + high) / 2

    if 'RUR' in currency:
        return avg_slr*1
    else:
        return avg_slr / get_currency_rate(currency)


#Разбиение списка запрлат на диапазоны
def get_salary_range(salaries):
    count = [0, 0, 0, 0, 0, 0]
    for salary in salaries:
        if salary < 60000:
            count[0] = count[0] + 1
        elif salary < 100000:
            count[1] = count[1] + 1
        elif salary < 140000:
            count[2] = count[2] + 1
        elif salary < 180000:
            count[3] = count[3] + 1
        elif salary < 250000:
            count[4] = count[4] + 1
        else:
            count[5] = count[5] + 1

    salary_range = {'<60k': count[0], '60-100k': count[1], '100-140k': count[2], '140-180k': count[3],
                    '180-250k': count[4],
                    '250k+': count[5]}
    return salary_range


#Получение кол-ва страниц найденых объявлений
def get_number_of_pages(request):
    return(request.json()).get('pages')


