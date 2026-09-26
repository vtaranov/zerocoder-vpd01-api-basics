# VPd01 — базовая работа с API

Домашнее задание к уроку «Что такое API и как с ним работать».

Программа выполняет GET-запрос к учебному JSONPlaceholder API, получает ответ в JSON и выводит три ключевых поля:

- имя пользователя;
- email;
- город.

## Почему выбран JSONPlaceholder

В уроке использовался REST Countries API версии 3.1, но эта версия больше не поддерживается. [Актуальная версия REST Countries](https://restcountries.com/docs/countries/api-versions) требует регистрацию и API-ключ.

Для базового задания выбран [JSONPlaceholder](https://jsonplaceholder.typicode.com/), потому что этот учебный API:

- работает без регистрации и API-ключа;
- возвращает понятный JSON-ответ;
- позволяет сосредоточиться на цели урока: GET-запросе, разборе JSON и выводе ключевых полей.

## Ручные GET-запросы

Эти URL можно открыть в браузере и увидеть JSON-ответ:

- https://jsonplaceholder.typicode.com/users/1
- https://jsonplaceholder.typicode.com/users/2
- https://jsonplaceholder.typicode.com/users/3

## Запуск

Требуется Python 3.9 или новее.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

Введите ID пользователя от `1` до `10`.

## Пример результата

```text
Ключевые поля:
Имя: Leanne Graham
Email: Sincere@april.biz
Город: Gwenborough
```
