from typing import List
from application.interfaces.event_request import Event
from domain.services.get_event_service import GetEventService


class GetEventUseCase():
    def __init__(
        self,
        get_service:GetEventService
        ):
        self.get_service=get_service

    async def execute(self,session_id:str=None):
        return await self.get_service.get_all_events(session_id)
