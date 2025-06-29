from fasthtml.common import * # type: ignore
from monsterui.all import * # type: ignore
from db import DB, ItemManager

db = DB()
itens = ItemManager(db)

itens.add_item("Mola da Grampona", 99)
itens.add_item("Mola dianteira", 59)
print(itens.search_item("Mola"))