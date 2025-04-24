from project.flask_server.database.db_utils import connect_db

class PlayerDAL:
    @staticmethod
    def add_player_dal(username: str, chat_id: int):
        conn = connect_db()
        cur = conn.cursor()
        try:
            stat = """INSERT INTO players (username, chat_id) VALUES (?, ?)"""
            cur.execute(stat, (username, chat_id))
            conn.commit()
        except Exception as e:
            print(f"Ошибка при создании пользователя: {e}")
            conn.rollback()
        finally:
            conn.close()

    @staticmethod
    def check_player_exists(chat_id) -> int:
        conn = connect_db()
        try:
            cur = conn.cursor()
            stat = """SELECT COUNT(*) FROM players WHERE  chat_id= ?"""
            count = cur.execute(stat, (chat_id,)).fetchone()[0]

            return count
        except Exception as e:
            print(f"Ошибка при поиске пользователя: {e }")
            return -1
        finally:
            conn.close()

    @staticmethod
    def return_top_players():
        conn = connect_db()
        try:
            cur = conn.cursor()
            stat = "SELECT username, coins_collected FROM players ORDER BY coins_collected DESC LIMIT 5"
            res = cur.execute(stat)

            return res.fetchall()
        except Exception as e:
            print(f"Ошибка при возврате пользователей: {e}")
        finally:
            conn.close()

