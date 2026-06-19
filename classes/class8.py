import sqlite3


# A4
connect = sqlite3.connect('order.db')
# Рука и карандаш
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (30) NOT NULL,
        age INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT NOT NULL,
        price INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
        )
''')
connect.commit()

def create_data():
    users = [
        ('Ardager', 27),
        ('Elina', 23),
        ('Logan', 23),
        ('Dean', 24),
    ]
    cursor.executemany(
        'INSERT INTO users(name, age) VALUES (?, ?)',
        users
    )
    connect.commit()
    print('users created')

# create_data()

def create_order():
    orders = [
        ("Iphone 17 pro max", 1250, 1),
        ("Samsung s25 ultra", 900, 2),
        ("Pixel 10 pro", 1000, 5),
    ]

    cursor.executemany(
        'INSERT INTO orders(product, price, user_id) VALUES (?, ?, ?)',
        orders
    )
    connect.commit()
    print('orders created')

# create_order()

def get_user_order():

    cursor.execute('''
        SELECT users.name, orders.product 
        FROM users INNER JOIN orders ON users.id = orders.user_id
    ''')
    data = cursor.fetchall()
    for i in data:
        print(f"name:{i[0]} product: {i[1]}")

# get_user_order()


# def get_sum_orders_price():
#
#     cursor.execute('''
#     SELECT * FROM orders
#     ''')
#     data = cursor.fetchall()
#     sum_price = 0
#     for i in data:
#         sum_price += i[2]
#     print(sum_price)
#
# get_sum_orders_price()

# def get_sum_orders_price():
#
#     cursor.execute('''
#     SELECT SUM(price) FROM orders
#     ''')
#     data = cursor.fetchall()
#     print(data)
#
# get_sum_orders_price()

# def get_sum_orders_price():
#
#     cursor.execute('''
#     SELECT AVG(price) FROM orders
#     ''')
#     data = cursor.fetchall()
#     print(data)
#
# get_sum_orders_price()

def get_sum_orders_price():
    # MAX(), MIN(), COUNT(), AVG(), SUM()
    cursor.execute('''
    SELECT COUNT(price) FROM orders
    ''')
    data = cursor.fetchone()
    print(data[0])

# get_sum_orders_price()

# create my view that gives a list of old users

def create_my_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS my_view AS
        SELECT users.name, orders.product, orders.price
        FROM users INNER JOIN orders WHERE users.age >  15
    ''')
    connect.commit()
    print('my_view created')

create_my_view()