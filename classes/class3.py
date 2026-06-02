# принципы ООП: Инкапсуляция, Абстракция. Гит - ветки
import random
import string
class BankAccount:
    def __init__(self, login, password, balance):
        self.login = login
        self.__password = password
        self._balance = balance

    def get_user_balance(self, password):
        if password == self.__password:
            return self._balance
        else:
            return 'Incorrect password'

    def __random_pass(self):
        data = string.ascii_letters + string.digits
        password = ''.join(random.choice(data) for i in range(6))
        return password

    def get_random_password(self):
        return self.__random_pass()

# class VIPAccount(BankAccount):
#     pass


# ardager = BankAccount('Ardager', '123321', '1000')

# print(ardager._BankAccount__password)
# print(ardager.get_random_password())
# print(dir(BankAccount))

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def make_sound(self):
        pass
    # @staticmethod

class Dog(Animal):
    def move(self):
        return 'Step'
    def make_sound(self):
        return 'woof'

gufi = Dog()
# print(gufi.make_sound())
# print(gufi.move())

class SendSms(ABC):
    @abstractmethod
    def send_otp_to_phone(self, phone):
        pass


class KGSendSms(SendSms):
    def request(self, data):
        pass

    def send_otp_to_phone(self, phone):
        data = f'''
            <Phone>{phone}</Phone>
            <Text>Ваш код; 123321</Text>
        '''
        self.request(data)


class RUSendSms(SendSms):
    def request(self, data):
        pass

    def send_otp_to_phone(self, phone):
        data = {
            'phone': phone,
            'text': 'Ваш код: 123321'
        }
        self.request(data)

