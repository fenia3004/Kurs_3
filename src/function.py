import json
import datetime

def load_operations():
    """список всех операций"""
    with open('operations.json', 'r', encoding="utf-8") as file:
        return json.load(file)


def last_operations(list_operations):
    """Вывод последних 5-ти операций"""
    list_convert_js = []
    counter = 0
    for i in list_operations:
        if i['state'] == 'EXECUTED':
            counter += 1
            list_convert_js.append(i)
            if counter == 5:
                break
    return list_convert_js


def modify_date(operation):
    """Форматирование даты"""
    data_list = operation['date']
    dt = datetime.datetime.fromisoformat(data_list)
    format_date = dt.date().strftime('%d.%m.%Y'), operation['description']
    return f'{" ".join(format_date)}'


def modify_card_to(operation):
    """Скрытие номера счета/карты куда переводят"""
    card_show_to = operation['to']
    name_card_to = card_show_to.split()[0]
    card_to = operation['to'][-4:].rjust(len(operation['to'][-6:]), "*")
    return f'{name_card_to} {card_to}'


def modify_card_from(operation):
    """Скрытие номера счета/карты от куда переводят"""
    card = operation['from']
    card_number = card.split()[-1]
    name_card = card.split()[0]
    return f'{name_card} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'

