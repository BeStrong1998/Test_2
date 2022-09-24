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
for i in school:
    men = 0
    women = 0
    for y in i['students']:  # перебираем студентов
        if is_male.get(y['first_name']) == False:  # если женский пол
            women += 1
        if is_male.get(y['first_name']) == True:  # если мужской пол
            men += 1
            
    if women > men:
        res = f"{'девочек'}"
    if women < men:
        res = f"{'мальчиков'}"

    print(f"Больше всего", res, f'в классе', f"{i['class']} \n", end='')

