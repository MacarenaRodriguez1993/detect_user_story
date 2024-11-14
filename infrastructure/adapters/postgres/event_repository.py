from typing import List
from sqlalchemy.orm import Session

from application.interfaces.event_request import Event
from domain.models.element_attribute_model import  ElementAttributeModel
from domain.models.event_model import EventModel
from domain.repository.event_repository import EventRepository
from domain.utils.detect_user_story import detectar_historias_generales

class PostgresEventRepository(EventRepository):
    def __init__(self, engine: Session):
        self.engine = engine

    async def save_events_repository(self,events:List[Event]):
        for event in events:
            event_model=EventModel(
                distinct_id = event.properties.distinct_id ,
                session_id = event.properties.session_id ,
                journey_id = event.properties.journey_id ,
                current_url = event.properties.current_url ,
                host = event.properties.host ,
                pathname = event.properties.pathname ,
                browser =event.properties.browser ,
                device = event.properties.device ,
                screen_height =event.properties.screen_height ,
                screen_width = event.properties.screen_width ,
                event_type =event.properties.eventType ,
                element_type = event.properties.elementType ,
                element_text = event.properties.elementText ,
                timestamp = event.properties.timestamp ,
                x = event.properties.x ,
                y = event.properties.y ,
                mouse_button = event.properties.mouseButton ,
                ctrl_key = event.properties.ctrlKey ,
                shift_key = event.properties.shiftKey ,
                alt_key = event.properties.altKey ,
                meta_key = event.properties.metaKey
            )
            self.engine.add(event_model)
            self.engine.commit()
            # ATTRIBUTES
            keys = list(event.properties.elementAttributes.keys())
            values = list(event.properties.elementAttributes.values())
            attributes=[]
            for i in range(len(keys)):
                attribute_model=ElementAttributeModel(
                    key= keys[i],
                    value=values[i],
                    event_id=event_model.id
                )
                self.engine.add(attribute_model)
                attributes.append(attribute_model)
            self.engine.commit()


    async def get_events_repository(self,session_id:str=None):
        if session_id==None:
            responses=self.engine.query(EventModel).all()
        else:
            responses=self.engine.query(EventModel).filter(EventModel.session_id==session_id).all()
        return responses