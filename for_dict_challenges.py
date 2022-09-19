# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
name1 = 0
name2 = 0
name3 = 0
for i in students:
    res = (i.get('first_name'))
    if res == 'Вася':
        name1 += 1
    if res == 'Петя':
        name2 += 1
    if res == 'Маша':
        name3 += 1
print(students[0]['first_name'] + ':', name1)
print(students[1]['first_name'] + ':', name2)
print(students[2]['first_name'] + ':', name3)




# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
num1 = 0
num2 = 0
num3 = 0
num4 = 0

for i in students:
    if i['first_name'] == 'Вася':
        num1 += 1
    if i['first_name'] == 'Петя':
        num2 += 1
    if i['first_name'] == 'Маша':
        num3 += 1
    if i['first_name'] == 'Оля':
        num4 += 1
if num2 < num1 > num3 and num4 < num1:
    print('Самое частое имя среди учеников:', students[0]['first_name'])
elif num1 < num2 > num3 and num4 < num2:
    print('Самое частое имя среди учеников:', students[1]['first_name'])
elif num1 < num3 > num2 and num4 < num3:
    print('Самое частое имя среди учеников:', students[2]['first_name'])
elif num1 < num4 > num2 and num3 < num4:
    print('Самое частое имя среди учеников:', students[3]['first_name'])



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

names = {}
names2 = {}
names3 = {}
num = 0
for student in school_students[0]:
    name = student['first_name']
    if name in names:
        names[name] += 1
    else:
        names[name] = 1
print('Самое частое имя в классе:', str(num + 1), max(names, key=names.get))

for student in school_students[1]:
    name = student['first_name']
    if name in names2:
        names2[name] += 1
    else:
        names2[name] = 1
print('Самое частое имя в классе:', str(num + 2), max(names2, key=names2.get))

for student in school_students[2]:
    name = student['first_name']
    if name in names3:
        names3[name] += 1
    else:
        names3[name] = 1
print('Самое частое имя в классе:', str(num + 3), max(names3, key=names3.get))




# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for i in school:
    print(f"Класс {i['class']}: ", end='')
    woman = 0
    men = 0
    for z in i['students']:
        if is_male.get(z['first_name']) == False:
            woman += 1
        if is_male.get(z['first_name']) == True:
            men += 1

    res = f"{woman} девочки и {men} мальчики"
    print(res)



# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

