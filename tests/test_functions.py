from src.function import modify_date, last_operations, modify_card_to, modify_card_from

test_list = {
    "id": 51314762,
    "state": "EXECUTED",
    "date": "2018-08-25T02:58:18.764678",
    "operationAmount": {
        "amount": "52245.30",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 4040551273087672",
    "to": "Visa Platinum 7825450883088021"
}

lol = {
    "id": 949194534,
    "state": "EXECUTED",
    "date": "2019-08-15T01:48:10.042554",
    "operationAmount": {
      "amount": "31222.43",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 65298957349197687907",
    "to": "Счет 38784565940893479418"
  }, {
    "id": 260972664,
    "state": "EXECUTED",
    "date": "2018-01-23T01:48:30.477053",
    "operationAmount": {
      "amount": "2974.30",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 3414396880443483",
    "to": "Visa Gold 2684274847577419"
  }, {
    "id": 317987878,
    "state": "EXECUTED",
    "date": "2018-01-13T13:00:58.458625",
    "operationAmount": {
      "amount": "55985.82",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 8906171742833215",
    "to": "Visa Platinum 6086997013848217"
  }, {
    "id": 72122709,
    "state": "EXECUTED",
    "date": "2018-12-18T17:07:09.800800",
    "operationAmount": {
      "amount": "19683.25",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 86675623828180311969",
    "to": "Счет 15351391408911677994"
  }, {
    "id": 242885401,
    "state": "EXECUTED",
    "date": "2019-07-08T00:08:32.986663",
    "operationAmount": {
      "amount": "10083.68",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 38427597486442637521",
    "to": "Счет 83889757415570699323"
  }


def test_modify_date():
    assert modify_date(test_list) == '25.08.2018 Перевод с карты на карту'
    assert type(modify_date(test_list)) == str


def test_modify_card_to():
    assert modify_card_to(test_list) == 'Visa **8021'
    assert type(modify_card_to(test_list)) == str


def test_modify_card_from():
    assert modify_card_from(test_list) == 'Visa 4040 55** **** 7672'
    assert type(modify_card_from(test_list)) == str


def test_last_operations():
    assert type(last_operations(lol)) == list
    assert len(last_operations(lol)) == 5