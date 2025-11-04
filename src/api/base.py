from abc import ABC, abstractmethod
from typing import Optional

class BaseAPI(ABC):
    @abstractmethod
    def search(self, query: str) -> Optional[str]:
        pass

    @abstractmethod
    def get_cover_url(self, item_id: Optional[str]) -> Optional[str]:
        pass 