from typing import List

from application.interfaces.event_request import Event
from domain.dtos.user_story import Actions, UserHistory
from domain.repository.event_repository import EventRepository
from domain.utils.detect_user_story import detectar_historias_generales


class GetEventService():
    def __init__(
        self,        
        repository:EventRepository
        ):
        self.repository=repository

    async def get_all_events(self,session_id:str=None):
        responses=await self.repository.get_events_repository(session_id)
        user_histories=detectar_historias_generales(responses)
        data_history=[]
        for index, history in enumerate(user_histories, start=1):
            for event in history['eventos']:
                element_attributes = event.element_attributes

                class_value = None
                href_value=None

                for attribute in element_attributes:
                    if attribute.key == 'class':
                        class_value = attribute.value
                        break 
                    if attribute.key == 'href':
                        href_value = attribute.value
                        break 
            data_history.append(
                UserHistory(
                    title=f'User history {index}',
                    actions=[
                        Actions(
                            type=event.element_type,
                            target=class_value if class_value else None,
                            value=href_value if href_value else None,  
                        )
                        for event in history['eventos']
                    ]
                )
            )
        return data_history