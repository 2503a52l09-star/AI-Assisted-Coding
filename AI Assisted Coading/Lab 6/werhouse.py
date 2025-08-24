    
class Product:
    """Represents a single product with name, price, and quantity."""

    def __init__(self, product_name: str, unit_price: float, units_in_stock: int):
        self.product_name = product_name
        self.unit_price = unit_price
        self.units_in_stock = units_in_stock

    def calculate_value(self) -> float:
        """Return the total value of this product (price × quantity)."""
        return self.unit_price * self.units_in_stock


class Warehouse:
    """Represents a warehouse that stores multiple products."""

    def __init__(self, warehouse_name: str):
        self.warehouse_name = warehouse_name
        self.inventory = []

    def add_product(self, new_product: Product):
        """Add a product to the warehouse inventory."""
        self.inventory.append(new_product)

    def total_value(self) -> float:
        """Return the total value of all products in the warehouse."""
        total = 0
        for item in self.inventory:
            total += item.calculate_value()
        return total

    def display_inventory(self):
        """Print a summary of products stored in the warehouse."""
        print(f"Warehouse: {self.warehouse_name}")
        for product in self.inventory:
            print(f"- {product.product_name}: {product.units_in_stock} units @ {product.unit_price} each")


# Example usage
if __name__ == "__main__":
    laptop = Product("Laptop", 950.0, 4)
    phone = Product("Phone", 450.0, 10)

    central_warehouse = Warehouse("Central Depot")
    central_warehouse.add_product(laptop)
    central_warehouse.add_product(phone)

    central_warehouse.display_inventory()
    print("Total value in warehouse:", central_warehouse.total_value())
