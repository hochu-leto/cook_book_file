# Денис Рудаков:
# Как бы я сделал:
# Заводим пустой словарь
# Создаем список с названиями ключей для словарей типа : key_ = ['ingredient_name', 'quantity', 'measure']
# Открываем файл
# Далее в цикле проходим по строкам
# Название блюда - первая строка
# Счетчик вложенного цикла - вторая строка
# Создаем пустой список
# Создаем еще один цикл в котором проходим до range(пункт 6 счетчик)
# Разделяем strip и split по знаку | строку
# Делаем zip с листам из пункта 2
# К пустому листу из пункта 7 += zip объект из пункта 10
# Далее cook_book[Название блюда] = список из 11 пункта
data = {}
key = ['ingredient_name', 'quantity', 'measure']
with open('c_book.txt', 'r', encoding='utf-8') as f:
    while True:
        # ingredients.clear()
        ingredients = []
        name = f.readline().rstrip()
        if not name:
            break
        ingredient_count = f.readline().rstrip()
        for i in range(int(ingredient_count)):
            ing = f.readline().rstrip()
            ing_list = ing.strip().split("|")
            ingredient = dict(zip(key, ing_list))
            ingredient['quantity'] = int(ingredient['quantity'])
            ingredients.append(ingredient)
        data[name] = ingredients
        f.readline().rstrip()
    print(data)


def get_shop_list_by_dishes(dishes, person_count):
    """

    :param dishes: список блюд из cook_book
    :param person_count: количество персон для кого мы будем готовить:
    :return: словарь с названием ингредиентов и его количества для блюда.
    типа
{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}
    """
    cook_dict = set()
    for dish in dishes:
        if dish in data:
            for ingredient in data[dish]:
                if ingredient in cook_dict:
                    cook_dict[ingredient]['quantity'] += data[dish][ingredient]['quantity']
                else
                    pass
