import func
import seaborn as sns
import matplotlib.pyplot as plt


#Диаграмма для диапазонов зарплат
def range_diagram(city_salary):
    sns.set(style="whitegrid", context="talk")

    f, ax = plt.subplots(figsize=(8, 6))
    sal_range = func.get_salary_range(city_salary.get('Москва'))

    sns.barplot(list(sal_range.keys()), list(sal_range.values()), palette="viridis", label='Ads')

    ax.set_ylabel("Ads quantity")
    ax.set_xlabel("Salary ranges(RUR)")
    ax.set_title("ML vacancies in Moscow")
    ax.legend()
    plt.show()


#Диаграмма для медианы зарплат по городам
def median_diagram(city_median_salary):
    sns.set(style="whitegrid", context="talk")
    f, ax = plt.subplots(figsize=(8, 6))

    i = 0

    keys = list(city_median_salary.keys())
    values = list(city_median_salary.values())
    keys_range = []
    values_range = []

    while i < 20:
        keys_range.append(keys[i])
        values_range.append(values[i])
        i = i+1

    sns.barplot(values_range, keys_range, palette="Blues_d", label='Salary')

    ax.set_ylabel("Cities")
    ax.set_xlabel("Salary (RUR)")
    ax.set_title("Median salary")
    ax.legend()
    plt.show()
