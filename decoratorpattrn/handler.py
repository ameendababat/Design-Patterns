from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def handle_request(self):pass