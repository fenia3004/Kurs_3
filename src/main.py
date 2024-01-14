from function import last_operations, modify_date, modify_card_to, modify_card_from, load_operations

# Вызов функции с файлом json
all_operations = load_operations()

# создание списка для дальнейшей работы
list_operations = []
for i in all_operations:
    list_operations.append(i)

# Вызов функции для выбора последних 5 чеков
operations = last_operations(list_operations)

# Сортировка по дате
operations.sort(key=lambda x: x.get('date'), reverse=True)

# Вывод всей полученной информации
for operation in operations:
    if operation.get('from'):
        print(modify_date(operation))
        print(modify_card_from(operation), '->', modify_card_to(operation))
        print(operation['operationAmount']['amount'], operation['operationAmount']['currency']['name'])
        print()
    else:
        print(modify_date(operation))
        print(modify_card_to(operation))
        print(operation['operationAmount']['amount'], operation['operationAmount']['currency']['name'])
        print()
