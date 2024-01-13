from function import last_operations, modify_date, modify_card_to, modify_card_from

operations = last_operations()
operations.sort(key=lambda x: x.get('date'), reverse=True)


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
