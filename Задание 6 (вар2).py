print('Привет, ученик курса GeekBrains!')
print('Предположим, что ты решил открыть свой бизнес, давай придумаем название товаров, которые ты будешь продавать, цену и количество штук в день.')

product = int(input("Введите количество товаров которое хочешь внести в каталог:"))
n = 1
my_dict = []
my_list = []
while n <= product:
    my_dict = dict({'название': input("Введите, пожалуйста, название товара:"), 'цена': input("Введите, пожалуйста, цену за товар в рублях:"),
                   'количество': input('Введите, пожалуйста, количество вашего товара:'), 'ед': input('Введите, пожалуйста, единицы измерения Вашего товара:')})
    my_list.append((n, my_dict))
    n += 1
print(my_list)
product_names = []
product_prices = []
product_amount = []
product_unit = []
for i in my_list:
    product_names.append(i[1].get('название'))
    product_prices.append(i[1].get('цена'))
    product_amount.append(i[1].get('количество'))
    product_unit.append(i[1].get('ед'))

my_analytics = {'название': (product_names),
    'цена': (product_prices), 'количество': (product_amount), 'ед': (product_unit)}
print('В итоге у нас получится такая занимательная аналитика:', my_analytics)
