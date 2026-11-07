from supplier import Supplier
from product import Product


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, download_size: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download size: {self.__download_size} MB")

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["Type"] = "digital"
        data["Download_size"] = self.__download_size
        return data
