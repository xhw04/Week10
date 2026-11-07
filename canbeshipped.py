
from abc import ABC, abstractmethod

# interface(must be able), only inherited in other classes


class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass
