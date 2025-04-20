import os
import sqlite3
from os import getenv

from dotenv import load_dotenv

load_dotenv()

def connect_db():
    connection = sqlite3.connect(getenv('DATABASE_PATH'))
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

def create_tables():
    execute_script(os.getenv('SQL_SCRIPT_PATH'))