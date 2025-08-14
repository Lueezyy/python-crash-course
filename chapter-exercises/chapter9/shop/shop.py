class Shop:
    def __init__(self, shop_name, shop_type):
        self.name = shop_name
        self.type = f'{shop_type} shop'
        self.sold = 20

    def describe_store(self):
        print(f'\nWelcome to {self.name}.')
        print(f'This is a {self.type}.')
    
    def open_store(self):
        print(f'\n{self.name} is now open.')

    def items_sold(self):
        print(f'\nItems sold at {self.name}: {self.sold}')

    def set_items_sold(self, sold):
        self.sold = sold

    def add_items_sold(self, sold):
        self.sold += sold

class Supermarket(Shop):
    def __init__(self, shop_name, shop_type='supermarket'):
        super().__init__(shop_name, shop_type)
        self.type = 'supermarket'
        self.categories = ['food', 'drinks', 'cleaning', 'health', 'household']

    def get_categories(self):
        print(f'\n{self.name} sells: {self.categories}')