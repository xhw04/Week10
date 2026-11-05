
from canbeshipped import CanBeShipped
from product import Product

# new child class from product,for weight

# class-object(passed from main)-parameter-attribute
# import product


class PhysicalProduct(Product, CanBeShipped):
    # create new attribute (weight)
    def __init__(self, product_id, name, price, stock, weight):
        # child class inherits from parent class, call parent constructor
        super().__init__(product_id, name, price, stock)
        # child class new attribute (weight)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight:{self.__weight}kg")

    def get_fulfilment_info(self):  # abstract method, called in child class
        return "This product requires physical shipping"

# calculate shipping cost based on weight (from abstract class CanBeShipped,called in childclass)
    def calculate_shipping_cost(self):
        return self.__weight * 2.5

# return as dict due to json (only here)
    def to_dict(self):
        data = super().to_dict()
        data["Type"] = "physical"
        data["Weight"] = self.__weight
        return data
