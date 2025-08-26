from abc import ABC,abstractmethod


class ScrollBar(ABC):
    @abstractmethod
    def draw(self):pass