from canbeshipped import CanBeShipped
from product import Product
from supplier import Supplier


# child class of Product, adds weight
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, weight: float):
        # call parent constructor
        super().__init__(product_id, name, price, stock, supplier)
        # child's own attribute
        self.__weight: float = weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    # abstract method from Product, implemented here
    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    # abstract method from CanBeShipped, implemented here
    def calculate_shipping_cost(self) -> float:
        return self.__weight * 2.5   # $2.50 per kg

    # return as dict due to json
    def to_dict(self) -> dict:
        data = super().to_dict()
        data["Type"] = "physical"
        data["Weight"] = self.__weight
        return data
