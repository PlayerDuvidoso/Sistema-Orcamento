from fasthtml.common import * # type: ignore
from monsterui.all import * # type: ignore
from db import DB, ItemManager

db = DB()
items = ItemManager(db)

items.add_item("Mola da Grampona", 99)
items.add_item("Mola dianteira", 59)
print(items.search_item("Mola"))