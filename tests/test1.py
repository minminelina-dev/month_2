from abc import ABC, abstractmethod
import random

class Hero(ABC):
    def __init__(self, name: str, lvl: int, hp: int):
        self.name = name
        self.lvl  = lvl
        self.hp   = hp

    @abstractmethod
    def action(self) -> str:
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, lvl={self.lvl})"


class MageHero(Hero):
    def __init__(self, name: str, lvl: int, hp: int, mp: int):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self) -> str:
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(MageHero):
    def action(self) -> str:
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

class BankAccount:
    bank_name = "Simba"

    def __init__(self, hero: Hero, balance: float, password: str):
        self.hero       = hero
        self._balance   = balance
        self.__password = password

    def login(self, password: str) -> bool:
        return self.__password == password

    @property
    def full_info(self) -> str:
        return (
            f"Герой: {self.hero.name} | "
            f"Класс: {self.hero.__class__.__name__} | "
            f"Уровень: {self.hero.lvl} | "
            f"Баланс: {self._balance} SOM"
        )

    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name

    def bonus_for_level(self) -> int:
        return self.hero.lvl * 10

    def __str__(self) -> str:
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other: "BankAccount"):
        if type(self.hero) is not type(other.hero):
            raise TypeError("Ошибка: Нельзя сложить счета героев разных классов!")
        return self._balance + other._balance

    def __eq__(self, other: "BankAccount") -> bool:
        return (
            type(self.hero) is type(other.hero)
            and self.hero.lvl == other.hero.lvl
        )

class KGSms:
    def send_otp(self, phone: str) -> str:
        otp = random.randint(100_000, 999_999)
        return f"[KGSms] Код подтверждения {otp} отправлен на {phone}"


if __name__ == "__main__":
    mage1    = MageHero("Merlin", lvl=50, hp=200, mp=150)
    mage2    = MageHero("Gandalf", lvl=50, hp=180, mp=120)
    warrior1 = WarriorHero("Conan", lvl=50, hp=300, mp=0)

    print(mage1.action())
    print(warrior1.action())

    acc1 = BankAccount(mage1,    balance=5000, password="secret123")
    acc2 = BankAccount(mage2,    balance=3000, password="pass456")
    acc3 = BankAccount(warrior1, balance=4000, password="sword789")

    print(acc1)
    print(acc2)
    print("Банк:", acc1.get_bank_name())
    print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

    print("\n=== Проверка __add__ ===")
    print("Сумма счетов двух магов:", acc1 + acc2)
    try:
        print("Сумма мага и воина:", acc1 + acc3)
    except TypeError as e:
        print(e)

    print("\n=== Проверка __eq__ ===")
    print("Mage1 == Mage2 ?", acc1 == acc2)
    print("Mage1 == Warrior ?", acc1 == acc3)

    sms = KGSms()
    print("\n", sms.send_otp("+996777123456"))