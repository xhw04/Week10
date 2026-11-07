from product import Product


class Inventory:
    def __init__(self) -> None:
        # aggregation: the inventory holds Product references
        self.__products: list[Product] = []

    def get_products(self) -> list[Product]:
        return self.__products

    def display_all(self) -> None:
        print("\nCurrent Inventory:")
        print("------------------")
        for item in self.__products:
            item.display_information()
        print("------------------")

    def find_product(self, product_id: str) -> Product | None:
        for item in self.__products:
            if item.get_product_id() == product_id:
                return item
        return None

    def add_product(self, product: Product) -> bool:
        if self.find_product(product.get_product_id()) is not None:
            print("Product ID already exists.")
            return False
        self.__products.append(product)
        return True

    # removes the reference only, the Product object still exists
    def remove_product(self, product_id: str) -> bool:
        item = self.find_product(product_id)
        if item is None:
            return False
        self.__products.remove(item)
        return True
