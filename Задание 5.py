print('Привет, ученик курса GeekBrains!')
print('Давай сыграем в игру!')
print('У меня есть список не возрастающих натуральных чисел')
my_list = [7, 5, 3, 3, 2]
print('Вот он -', my_list)
print('Давай ты будешь придумывать новые числа, а я буду расставлять их в порядке убывания в свой список!')
n = int(input('Введи, пожалуйста, одно натуральное число:'))
my_list.append(n)
you_list = []
while len(my_list) > 0:
    you_list.append(max(my_list))
    my_list.remove(max(my_list))
my_list = you_list
print('С твоим числом получается такой список', my_list)