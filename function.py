import json, os.path
import datetime


def load_operations():
    """список всех операций"""
    operations_json = os.path.join('src', 'operations.json')
    with open(operations_json, 'r', encoding="utf-8") as file:
        convert_js = json.load(file)
        return convert_js


convert_js = load_operations()


def last_operations():
    """Вывод последних 5-ти операций"""
    list_convert_js = []
    counter = 0
    for i in convert_js:
        if i['state'] == 'EXECUTED':
            counter += 1
            list_convert_js.append(i)
            if counter == 5:
                break
    return list_convert_js


def modify_date(operation):
    data_list = operation['date']
    dt = datetime.datetime.fromisoformat(data_list)
    format_date = dt.date().strftime('%d.%m.%Y'), operation['description']
    return f'{" ".join(format_date)}'


def modify_card_to(operation):
    card_show_to = operation['to']
    name_card_to = card_show_to.split()[0]
    card_to = operation['to'][-4:].rjust(len(operation['to'][-6:]), "*")
    return f'{name_card_to} {card_to}'


def modify_card_from(operation):
    card = operation['from']
    card_number = card.split()[-1]
    name_card = card.split()[0]
    return f'{name_card} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'