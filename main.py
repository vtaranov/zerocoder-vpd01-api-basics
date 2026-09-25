"""Базовая работа с JSONPlaceholder API."""

import json

import requests


API_URL = "https://jsonplaceholder.typicode.com/users/{user_id}"


def get_user(user_id: int) -> dict:
    """Запрашивает данные пользователя и возвращает JSON-объект."""
    response = requests.get(API_URL.format(user_id=user_id), timeout=10)
    response.raise_for_status()

    user = response.json()
    if not user:
        raise ValueError("В ответе API нет данных о пользователе.")

    return user


def print_user(user: dict) -> None:
    """Выводит JSON и три ключевых поля о пользователе."""
    print("\nJSON-ответ:")
    print(json.dumps(user, ensure_ascii=False, indent=2))

    print("\nКлючевые поля:")
    print(f"Имя: {user.get('name', 'нет данных')}")
    print(f"Email: {user.get('email', 'нет данных')}")
    print(f"Город: {user.get('address', {}).get('city', 'нет данных')}")


def main() -> None:
    raw_user_id = input("Введите ID пользователя от 1 до 10: ").strip()

    try:
        user_id = int(raw_user_id)
    except ValueError:
        print("Ошибка: ID должен быть целым числом.")
        return

    try:
        user = get_user(user_id)
        print_user(user)
    except requests.HTTPError as error:
        if error.response is not None and error.response.status_code == 404:
            print("Ошибка: пользователь с таким ID не найден.")
        else:
            print(f"Ошибка HTTP: {error}")
    except requests.RequestException as error:
        print(f"Не удалось выполнить запрос: {error}")
    except (TypeError, ValueError, KeyError) as error:
        print(f"Не удалось обработать JSON-ответ: {error}")


if __name__ == "__main__":
    main()
