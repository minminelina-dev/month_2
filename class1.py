# def test():
#     print('test')
#
# test()

class Hero:

    # class constructor
    def __init__(self, name, level, hp):
        # class atributes
        self.name = name
        self.level = level
        self.hp = hp

    # class methods
    def rest(self):
        return f'{self.name} chilling and resting'

# class based object
kirito = Hero('Kirito', 100, 1000)
asuna = Hero('Asuna', 111, 1111)

print(kirito.rest())


# my_int = 123

# print(type(my_int))
# print(type(kirito))

# print(kirito.name)
# print(kirito.level)
# print(kirito.hp)

