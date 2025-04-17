import sqlite3

def connect_db():
    connection = sqlite3.connect('database.db')
    return connection

def execute_script(sql_path):
    with open(sql_path, 'r', encoding='utf8') as f:
        sql = f.read()

    conn = connect_db()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("Таблица базы данных успешно создана!")

    except Exception as e:
        print(f"Ошибка при создании таблицы баз данных: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    execute_script("../sql/scripts.sql")
