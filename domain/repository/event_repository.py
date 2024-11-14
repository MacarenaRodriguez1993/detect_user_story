from abc import ABC, abstractmethod
from typing import List

from application.interfaces.event_request import Event


class EventRepository(ABC):
    @abstractmethod
    def save_events_repository(self,events:List[Event]):
        pass

    @abstractmethod
    def get_events_repository(self,session_id:str=None):
        pass