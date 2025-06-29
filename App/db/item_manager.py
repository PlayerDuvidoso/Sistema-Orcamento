import sqlite3
from .database import DB
from .models import Item

class ItemManager: #    Create, Update and Delete the itens in the table
    def __init__(self, db: DB) -> None:
        self.database = db
        self.cur: sqlite3.Cursor = self.database.cur
        self.item_table: str = self.database.itens_table[0]
    

    def add_item(self, item_description: str, item_price: float) -> bool:
        if item_description and item_price: #   Checks if there is a description and price
            self.cur.execute(f"INSERT INTO {self.item_table} VALUES(null, ?, ?)", (item_description, item_price,))
            self.commit_changes()
            return True
        return False


    def update_item(self, item_id: int, new_description: str | None = None, new_price: float | None = None) -> Item | None:
        if self.get_item(item_id): #    Checks if the item_id exists
            if new_description is None and new_price is None: # If there is nothing to update return
                return None
            self.cur.execute(f"""UPDATE {self.item_table}
                             SET
                                description = COALESCE(?, description),
                                price = COALESCE(?, price)
                             WHERE id=?""", (new_description, new_price, item_id))
            self.commit_changes()
            return self.get_item(item_id)
        return None


    def delete_item(self, item_id: int) -> Item | None:
        if item := self.get_item(item_id): #    Checks and instance if the item exists
            self.cur.execute(f"DELETE FROM {self.item_table} WHERE id=?", (item_id,))
            self.commit_changes()
            return item
        return None


    def search_item(self, query: str) -> list[Item | None]:
        '''Returns a list of items that contains the specified query.'''
        data_list = self.cur.execute(f"SELECT * FROM {self.item_table} WHERE description LIKE '%{query}%'").fetchall()
        items = []
        for item_data in data_list:
            items.append(Item(id=item_data[0], description=item_data[1], price=item_data[2]))
        return items
    

    def get_item(self, item_id: int) -> Item | None:
        if item_data := self.cur.execute(f"SELECT * FROM {self.item_table} WHERE id=?", (item_id,)).fetchone():
            item = Item(id=item_data[0], description=item_data[1], price=item_data[2])
            return item
        return None
    

    def commit_changes(self):
        self.database.con.commit()