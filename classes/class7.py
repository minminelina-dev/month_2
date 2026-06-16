import sqlite3


# A4
connect = sqlite3.connect('user.db')
# Рука и карандаш
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()

# CRUD - create - read - update - delete

def create_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print('user created successfully')

# create_user('Elina', 23, 'travelling, yoga')
# create_user('Suga', 66, 'travelling, yoga')
# create_user('Ardager', 27, 'travelling, yoga')
# create_user('Logan', 23, 'travelling, yoga')

def get_users():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    print(data)

get_users()

def update_user(name, rowid):
    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (name, rowid)
    )
    connect.commit()
    print('user updated successfully')

update_user('John Logan', 3)

def delete_user(rowid):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (rowid,)
    )
    connect.commit()
    print('user deleted successfully')

# delete_user(3)