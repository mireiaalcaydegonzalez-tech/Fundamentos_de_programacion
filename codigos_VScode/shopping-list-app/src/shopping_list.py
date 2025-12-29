class ShoppingList:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def display_list(self):
        if not self.items:
            print("La lista de compras está vacía.")
        else:
            print("Lista de compras:")
            for product, quantity in self.items.items():
                print(f"{product}: {quantity}")

    def finalize_list(self):
        return self.items.copy()