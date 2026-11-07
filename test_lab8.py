from supplier import Supplier
from product import Product
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from inventory import Inventory
from order import Order


def section(title: str) -> None:
    print(f"\n=== {title} ===")


# LSP: works with ANY Product
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


# ---------- 1. ASSOCIATION (Supplier and Product) ----------
section("1. Association: Supplier and Product")
supplier = Supplier("S001", "TechSupply", "sales@techsupply.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, supplier, 2.1)
game = DigitalProduct("P002", "Game", 59.90, 100, supplier, 2048)

print("Both products share the same supplier object?",
      laptop.get_supplier() is game.get_supplier())
laptop.get_supplier().display_information()

del supplier   # Predict First #1
print("\nAfter del supplier, products still show it:")
laptop.get_supplier().display_information()
game.get_supplier().display_information()

# ---------- 2. AGGREGATION (Inventory and Product) ----------
section("2. Aggregation: Inventory and Product")
mouse = PhysicalProduct("P003", "Mouse", 25.50, 40,
                        Supplier("S002", "PeriphCo", "hi@periphco.com"), 0.1)
inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(mouse)
print("In A:", inventory_a.find_product("P003") is mouse)

inventory_a.remove_product("P003")   # Predict First #2
print("In A after removal:", inventory_a.find_product("P003"))
print("Mouse still works after removal:")
mouse.display_information()

inventory_b.add_product(mouse)
print("Same object now in B:", inventory_b.find_product("P003") is mouse)

# ---------- 3. COMPOSITION (Order and OrderLine) ----------
section("3. Composition: Order and OrderLine")
order1 = Order("O001")
order1.add_order_line(laptop, 1)
order1.add_order_line(game, 2)
order1.display_information()

order2 = Order("O002")
order2.add_order_line(laptop, 3)   # same product, different order

line_a = order1.get_order_lines()[0]
line_b = order2.get_order_lines()[0]
print("\nPredict First #3")
print("Same OrderLine object?", line_a is line_b)
print("Same Product object?", line_a.get_product() is line_b.get_product())

order1.remove_order_line(0)
print("\nOrder O001 after removing line 0:")
order1.display_information()
print("Laptop still exists:", laptop.get_product_id())

# ---------- 4. POLYMORPHISM AND LSP ----------
section("4. Polymorphism and LSP")
inventory = Inventory()
inventory.add_product(laptop)
inventory.add_product(game)

print("Predict First #4: one loop, no isinstance")
for product in inventory.get_products():
    product.display_information()
    print(product.get_fulfilment_info())

print("\nshow_product_details works for both:")
show_product_details(laptop)
show_product_details(game)

print("\nBoth subclasses keep the update_stock promise:")
for product in inventory.get_products():
    print(product.get_product_id(), "update_stock(50) ->",
          product.update_stock(50))
    print(product.get_product_id(), "update_stock(-1) ->",
          product.update_stock(-1))

# ---------- 5. ABSTRACT CLASS ----------
section("5. Product cannot be created directly")
try:
    Product("P999", "Test", 1.0, 1, Supplier("S9", "X", "x@x.com"))
except TypeError as error:
    print("TypeError:", error)
