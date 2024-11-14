from typing import List
from application.interfaces.event_request import Event
from domain.services.save_event_service import SaveEventService


class SaveEventUseCase():
    def __init__(
        self,
        save_service:SaveEventService
        ):
        self.save_service=save_service

    async def execute(self,event_payload:List[Event]):
        return await self.save_service.save_new_events(event_payload)
