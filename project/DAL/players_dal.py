from project.database.db_utils import connect_db

class PlayerDAL:
    @staticmethod
    def add_player_dal(username: str, chat_id: int,  x, y):
        conn = connect_db()
        cur = conn.cursor()
        try:
            stat = """INSERT INTO players (username, chat_id,  x, y) VALUES (?, ?, ?, ?)"""
            cur.execute(stat, (username, chat_id, x, y))
            conn.commit()
        except Exception as e:
            print(f"Ошибка при создании пользователя: {e}")
            conn.rollback()
        finally:
            conn.close()

    @staticmethod
    def check_player_exists(chat_id):
        conn = connect_db()
        try:
            cur = conn.cursor()
            stat = """SELECT COUNT(*) FROM players WHERE chat_id = ?"""
            res = cur.execute(stat, (chat_id,))

            return res.fetchone()[0]
        except Exception as e:
            print(f"Ошибка при поиске пользователя: {e }")
        finally:
            conn.close()

