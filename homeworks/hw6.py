# Часть 1 — Внешние зависимости
# Используем библиотеку faker

from faker import Faker

# Эта библиотека нужна для генерации случайных "фейковых" данных:
# имён, адресов, email-адресов, номеров телефонов, дат рождения и т.д.
# Она часто используется для тестирования программ и баз данных,
# когда нужны реалистичные, но не настоящие данные пользователей.

fake = Faker()
# Чтобы имена/адреса генерировались на русском языке, можно использовать:
# fake = Faker("ru_RU")

def generate_users(count: int = 5) -> list[dict]:
    """Генерирует список фейковых пользователей."""
    users = []
    for _ in range(count):
        user = {
            "name": fake.name(),
            "email": fake.email(),
            "address": fake.address().replace("\n", ", "),
            "phone": fake.phone_number(),
            "birthdate": str(fake.date_of_birth(minimum_age=18, maximum_age=65)),
        }
        users.append(user)
    return users


if __name__ == "__main__":
    users = generate_users(5)
    for i, user in enumerate(users, start=1):
        print(f"Пользователь {i}:")
        for key, value in user.items():
            print(f"  {key}: {value}")
        print()