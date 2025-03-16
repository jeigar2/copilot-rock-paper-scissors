import sqlite3

def init_db():
    conn = sqlite3.connect('game_stats.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stats
                 (id INTEGER PRIMARY KEY, user_choice INTEGER, computer_choice INTEGER, result TEXT)''')
    conn.commit()
    conn.close()

def record_game(user_choice, computer_choice, result):
    conn = sqlite3.connect('game_stats.db')
    c = conn.cursor()
    c.execute("INSERT INTO stats (user_choice, computer_choice, result) VALUES (?, ?, ?)",
              (user_choice, computer_choice, result))
    conn.commit()
    conn.close()

def get_stats():
    conn = sqlite3.connect('game_stats.db')
    c = conn.cursor()
    c.execute("SELECT user_choice, computer_choice, result FROM stats")
    rows = c.fetchall()
    conn.close()
    return rows