import sqlite3

class DB:
    def __init__(self):
        self.con = sqlite3.connect(f"App/SORC.db")
        self.cur = self.con.cursor()
        
        self.itens_table: tuple[str] = self.add_table("itens") #  Creates the table if not already


    def add_table(self, table_name: str) :
        table: tuple | None = self.get_table(table_name)
        
        if not table: #    Check if the table already exist, and creates it if not present
            self.cur.execute(f"CREATE TABLE {table_name}(id INTEGER PRIMARY KEY AUTOINCREMENT, description NOT NULL, price NOT NULL)")
            return self.cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,)).fetchone()
        
        return table
    
    
    def get_table(self, table_name: str) -> tuple | None:
        return self.cur.execute(f"SELECT name FROM sqlite_master WHERE name='{table_name}'").fetchone()