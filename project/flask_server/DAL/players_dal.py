from project.flask_server.database.db_utils import connect_db

class PlayerDAL:
    @staticmethod
    def add_player_dal(chat_id: int, username: str):
        conn = connect_db()
        cur = conn.cursor()
        try:
            stat = """INSERT INTO players (chat_id, username) VALUES (?, ?)"""
            cur.execute(stat, (chat_id, username))
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

    @staticmethod
    def get_coordinate(chat_id: int):
        conn = connect_db()
        try:
            cur = conn.cursor()
            stat = """SELECT X, Y FROM players where chat_id = ?"""
            player = cur.execute(stat, (chat_id,)).fetchone()

            if player:
                return {"x": player[0], "y": player[1]}
            else:
                return None
        except Exception as e:
            print(f"Ошибка при получении координат: {e}")
        finally:
            conn.close()

    @staticmethod
    def coordinate_change(chat_id, x: int, y: int):
        conn = connect_db()
        try:
            cur = conn.cursor()
            stat = """UPDATE players SET x = ?, y = ? WHERE chat_id = ?"""
            cur.execute(stat, (x, y, chat_id))
            conn.commit()

            return True
        except Exception as e:
            print(f"Произошла ошибка при изменении координат: {e}")
            conn.rollback()

            return False
        finally:
            conn.close()