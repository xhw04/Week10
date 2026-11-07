from supplier import Supplier
from product import Product


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, download_size: int):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: int = download_size

    def display_information(self):
        super().display_information()
        print(f"Download size:{self.__download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."

    def to_dict(self):
        data = super().to_dict()
        data["Type"] = "digital"
        data["Download_size"] = self.__download_size
        return data
