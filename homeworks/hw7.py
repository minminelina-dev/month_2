import sqlite3

# A4
connect = sqlite3.connect('store.db')
# Рука и карандаш
cursor = connect.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            name     TEXT    NOT NULL,
            price    REAL    NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)
    connect.commit()

def create_product(name, price, quantity):
    cursor.execute(
        'INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)',
        (name, price, quantity)
    )
    connect.commit()
    print(f"Товар '{name}' добавлен.")

def read_products():
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    if not rows:
        print('Таблица пуста.')
        return
    for row in rows:
        print(row)

def update_product(product_id, price):
    cursor.execute(
        'UPDATE products SET price = ? WHERE id = ?',
        (price, product_id)
    )
    connect.commit()
    print(f'Цена товара id={product_id} обновлена.')

def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    connect.commit()
    print(f'Товар id={product_id} удалён.')


create_table()

create_product('Книга Р. Куанг "История Тайпея"',    3000, 10)
create_product('Книга Л. Толстой "Война и мир"',         1000, 50)
create_product('Книга Д. Роулинг "Гарри Поттер"',   1500, 30)
create_product('Книга Р. Куанг "Вавилон"',     2200,  8)

read_products()

update_product(1, 2900)
update_product(2,   900)

read_products()

delete_product(1)
delete_product(2)
delete_product(3)

read_products()