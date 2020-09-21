cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[0]},
            {'user': users[1], 'city': cities[1]},
            {'user': users[2], 'city': cities[2]}]

city = input('Введите город: ').capitalize()


#создаём переменную user_data, чтобы при помощи функции append добавлять сюда данные
user_data = []


#проверяем, ввел ли данные пользователь. Если поле не заполнено, то программа выдаст "Вы не указали город" 
try:
    city[0]
#задаем условие, которое будет действовать в случае, если введенного города не будет в списке
    if city not in cities:
        print('Такого города нет в списке')
#при помощи цикла for проходимся по данным в переменной tourists и если заданное условие if внутри цикла оказывается верным, то данные добавляем в переменную user_data
    for i in tourists:
        if city in i['city']:
            user_data.append(i)
            print(f"Турист {user_data[0]['user']['name']} возраст {user_data[0]['user']['age']}. Посетил город {user_data[0]['city']}")
except IndexError:
    print('Вы не указали город')
