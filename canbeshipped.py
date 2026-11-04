
from abc import ABC, abstractmethod

# abstract class, cannot be instantiated, only inherited in other classes


class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass
