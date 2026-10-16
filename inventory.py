
from product import Product


class Inventory:
    def __init__(self):
        self.products = {}

    def add(self, product):
        if not isinstance(product, Product):
            raise TypeError("Expected a Product object")
        if product.sku in self.products:
            raise ValueError("Product SKU already exists")
        self.products[product.sku] = product

    def remove(self, sku):
        return self.products.pop(sku, None)

    def find(self, sku):
        return self.products.get(sku)

    def total_value(self):
        return sum(
            product.line_value
            for product in self.products.values()
        )

    @classmethod
    def from_lines(cls, lines):
        inventory = cls()
        for line in lines:
            product = Product.from_csv_line(line)
            inventory.add(product)
        return inventory