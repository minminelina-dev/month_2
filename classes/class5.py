
class Math:

    @staticmethod
    def add(a, b):
        return a + b

obj_test = Math()
print(Math.add(12, 12))

class Bank:
    # class atributes
    name = 'MBank'

    def __init__(self, value):
        # attributes of class exampler
        self.value = value

    def get_value(self):
        return self.value

    @classmethod
    def get_name(cls):
        return cls.name

    @classmethod
    def base_create(cls):
        return cls('Base value')

bank = Bank('Ardager')
bank_1 = Bank.base_create()

# print(bank.get_value())
# print(bank.get_name())
# print(bank_1.get_value())
# print(bank_1.get_name())

class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price must be positive')
        self.__price = value

    def get_price(self):
        return self.__price

iphone = Product(1250)

iphone.price = 200
print(iphone.price)

# print(iphone.get_price())
# print(iphone.price)
# print(iphone.__price)



