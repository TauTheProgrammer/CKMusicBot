from abc import ABC, abstractmethod


class QueryService(ABC):
    @abstractmethod
    def query(self, media: str):
        pass
