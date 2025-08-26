from abc import ABC, abstractmethod


class NotificationOpserver(ABC):
    @abstractmethod
    def update(self, order):pass