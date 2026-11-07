from product import Product


class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        # association: the line refers to a Product but does not own it
        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> None:
        print(f"  {self.__quantity} x {self.__product.get_name()} "
              f"= ${self.calculate_subtotal():.2f}")


class Order:
    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        # composition: the Order owns its OrderLine objects
        self.__order_lines: list[OrderLine] = []

    # the Order creates the OrderLine itself
    def add_order_line(self, product: Product, quantity: int) -> None:
        self.__order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, index: int) -> bool:
        if 0 <= index < len(self.__order_lines):
            self.__order_lines.pop(index)
            return True
        return False

    def get_order_lines(self) -> list[OrderLine]:
        return self.__order_lines

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.__order_lines)

    def display_information(self) -> None:
        print(f"Order {self.__order_id}")
        for line in self.__order_lines:
            line.display_information()
        print(f"  Total: ${self.calculate_total():.2f}")
