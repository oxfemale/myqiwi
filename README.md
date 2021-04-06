# myqiwi

[![Build Status](https://travis-ci.com/daveusa31/myqiwi.svg?branch=master)](https://travis-ci.com/daveusa31/myqiwi)
[![PyPi Package Version](https://img.shields.io/pypi/v/myqiwi.svg?style=flat-square)](https://pypi.python.org/pypi/myqiwi)
[![PyPi status](https://img.shields.io/pypi/status/myqiwi.svg?style=flat-square)](https://pypi.python.org/pypi/myqiwi)
[![Downloads](https://pepy.tech/badge/myqiwi)](https://pepy.tech/project/myqiwi)
[![Supported python versions](https://img.shields.io/pypi/pyversions/myqiwi.svg?style=flat-square)](https://pypi.python.org/pypi/myqiwi)


Возможности
======
* Переводы на любой Qiwi Кошелек
* Статистика по платежам
* Получение информации о пользователе
* Сортировка платежей по типу(в/из), валюте.
* Определение провайдера мобильного телефона


Использование
======
```python
import myqiwi
wallet = myqiwi.Wallet(token)
```

Быстрый туториал
======

Получить текущий баланс
----------------
```python
print(wallet.balance())
```

Отправка платежа
----------------
```python
payee = "7999778909" # Получатель платежа
sum = 50 # Сумма перевода. Обязательно в рублях!
comment = "Перевод сделан с помощью библиотеки myqiwi" # Необязательный аргумент

wallet.send_money(payee,sum,comment)
```

Генерация комментария и ожидание платежа
----------------

```python
need_sum = 100
resp = qiwi.gen_payment(need_sum) # Генерируем комментарий и ссылку к платежу

text = "Переведите {} рублей на номер {}, указав в комментариях {}"
text = text.format(need_sum, phone, resp["comment"])
print(text)
print("Ссылку на форму с оплатой: {}".format(resp["link"]))

payment = qiwi.search_payment(resp["comment"], need_sum=need_sum)

if payment["status"]:
    print("Поступило пополнение на сумму {} рублей!".format(payment["sum"]))
else:
    print("Пополнения не обнаружено! :(")
```


# To do
- [ ] Добавить возможность установки хендлера, для получения уведомлений о новых транзакциях
- [ ] Добавить файл utils. Куда перенести собственные функции
- [ ] Написать таблицу с методами, описанием и передаваемыми аргументами
- [ ] Переписать readme
- [X] Добавить свойство username
- [X] Добавить поддержку прокси 06.08.20
- [X] Переписать функцию generate_pay_form 08.07.20
- [X] Добавить возможность вывода ошибок в транслите, с помощью библиотеки [transliterate](https://github.com/barseghyanartur/transliterate) 04.07.20
