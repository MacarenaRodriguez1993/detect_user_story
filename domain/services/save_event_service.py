from typing import List

from application.interfaces.event_request import Event
from domain.repository.event_repository import EventRepository


class SaveEventService():
    def __init__(
        self,        
        repository:EventRepository
        ):
        self.repository=repository

    async def save_new_events(self,event_payload:List[Event]):
       return  await self.repository.save_events_repository(event_payload)