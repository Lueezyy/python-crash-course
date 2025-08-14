from shop import Shop, Supermarket

greggs = Shop("Gregg's", 'bakery')
coop = Shop('Co-Op', 'supermarket')
primark = Shop('Primark', 'clothing')
sainsburys = Shop("Sainsbury's", 'supermarket')

print(greggs.name)
print(greggs.type)

greggs.describe_store()
greggs.open_store()
coop.describe_store()
primark.describe_store()
sainsburys.describe_store()

greggs.items_sold()
greggs.set_items_sold(500)
greggs.items_sold()
greggs.add_items_sold(390)
greggs.items_sold()

aldi = Supermarket('Aldi')
aldi.describe_store()
aldi.get_categories()