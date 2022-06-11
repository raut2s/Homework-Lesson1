print('Привет, ученик курса GeekBrains!')
list = int(input(
    'Введи номер месяца и я смогу сказать к какому времени года он относится:'))
dict_year = {'key_1': 'зима', 'key_2': 'весна',
    'key_3': 'лето', 'key_4': 'осень'}
while list < 1 or list > 12:
    print('Я ЖЕ СКАЗАЛ ВВЕСТИ ЦИФРУ ОТ 1 до 12! ОПЯТЬ НЕ СЛУШАЕШЬ МЕНЯ!')
    list = int(input('Введи номер месяца и я смогу сказать к какому времени года он относится:'))
    continue
if list == 12 or list == 1 or list == 2:
    print(dict_year['key_1'])
elif list == 3 or list == 4 or list == 5:
    print(dict_year['key_2'])
elif list == 6 or list == 7 or list == 8:
    print(dict_year['key_3'])
else:
    print(dict_year['key_4'])
