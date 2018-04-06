import statistics
import requests
import func
import diagram


param = {'text': 'Машинное обучение', 'vacancy_search_fields': 'name', 'per_page': '100', 'only_with_salary': 'true'}
general_request = requests.get('https://api.hh.ru/vacancies/', param)
i = 0
counter = 0

avg_salary = [] #список для хранения средней зарплаты из вилки
city_salary = {} #словарь для хранения городов и списка их зарплат
city_median_salary = {} #словарь для хранения городов и медианы зарплат

#Заполнение словаря городов и зарплат значениями
while i < func.get_number_of_pages(general_request) - 2:

    param = {'text': 'Машинное обучение', 'vacancy_search_fields': 'name', 'per_page': '100',
             'only_with_salary': 'true', 'page': i}

    req = requests.get('https://api.hh.ru/vacancies/', param)
    items = (req.json()).get('items')

    if items is not None:
        for item in items:

            salary = item.get('salary')
            city_id = (item.get('area')).get('name')
            avg_salary.append(func.get_avg_salary(salary.get('from'), salary.get('to'), salary.get('currency')))

            #Создание списка, если в словаре еще нет такого города
            if city_salary.get(city_id) is None:
                temp = [avg_salary[counter]]
                city_salary[city_id] = temp

            #Добавление в список зарплаты конкретного города
            else:
                temp = (city_salary.get(city_id))
                temp.append(avg_salary[counter])
                city_salary[city_id] = temp

            counter = counter + 1

    else:
        break

    i = i + 1

#Вычисление медианы для каждого города
for x in city_salary.keys():
    city_median_salary[x] = statistics.median(city_salary.get(x))

#Построение диаграмм
diagram.range_diagram(city_salary)
diagram.median_diagram(city_median_salary)
