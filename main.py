
from inventory import Inventory
from product import Product


SAMPLE = [
    "Milk,MLK001,1.25,12",
    "Bread,BRD002,0.90,3",
    "Eggs,EGG003,2.40,30",
    "Coffee,COF004,7.50,2",
]


def main():
    inventory = Inventory.from_lines(SAMPLE)

    print("=== MiniMart Inventory Report ===")

    for product in inventory.products.values():
        print(
            f"{product.name:10} "
            f"SKU: {product.sku} "
            f"Price: ${product.price:.2f} "
            f"Quantity: {product.quantity} "
            f"Value: ${product.line_value:.2f}"
        )

    print("-" * 50)
    print(f"Total inventory value: ${inventory.total_value():.2f}")

    print("\nLow-stock products:")
    for product in inventory.products.values():
        if product.is_low_stock:
            print(f"- {product.name} ({product.quantity} left)")

    print(f"\nProducts created: {Product.count()}")


if __name__ == "__main__":
    main()