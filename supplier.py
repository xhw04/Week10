# 3 attrribute for product.py,added type hinting
class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = contact_email

# get supplier id info for product
    def get_supplier_id(self):
        return self.__supplier_id

    def display_information(self):
        print(f"ID:{self.__supplier_id} | Name:{self.__name} |"
              f"Email:{self.__contact_email}"
              )

    def to_dict(self) -> dict:
        return {"ID": self.__supplier_id, "Name": self.__name,
                "Email": self.__contact_email}
