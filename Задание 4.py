print('Привет, ученик курса GeekBrains!')
list = input(
    'Введи элементы для списка (несколько слов), разделынные пробелами:').split()
print(list)
for ind, i in enumerate(list):
    if len(i) <= 10:
        print(ind, i)
    else:
        i1 = i[0:10]
        print(ind, i1)

