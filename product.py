
class Product:
    _count = 0

    def __init__(self, name, sku, price, quantity):
        self.name = name
        self.sku = sku
        self.price = price
        self.quantity = quantity

        if not self.is_valid_sku(sku):
            raise ValueError("Invalid SKU")

        Product._count += 1

    def __repr__(self):
        return (
            f"Product({self.name!r}, {self.sku!r}, "
            f"{self.price!r}, {self.quantity!r})"
        )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if type(value) is not int or value < 0:
            raise ValueError(
                "Quantity must be a non-negative integer"
            )
        self._quantity = value

    @property
    def line_value(self):
        return self.price * self.quantity

    @property
    def is_low_stock(self):
        return self.quantity < 5

    @classmethod
    def from_csv_line(cls, line):
        name, sku, price, quantity = line.strip().split(",")
        return cls(name.strip(), sku.strip(),
                   float(price), int(quantity))

    @staticmethod
    def is_valid_sku(sku):
        return (
            isinstance(sku, str)
            and len(sku) == 6
            and sku[:3].isalpha()
            and sku[:3].isascii()
            and sku[:3].isupper()
            and sku[3:].isdigit()
            and sku[3:].isascii()
        )

    @classmethod
    def count(cls):
        return cls._count