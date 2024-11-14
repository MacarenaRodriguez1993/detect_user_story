from sqlalchemy import Column, String, Integer, Boolean,  Text
from sqlalchemy.orm import relationship
from data_base_config import Base
from domain.models.element_attribute_model import ElementAttributeModel



class EventModel(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    distinct_id = Column(String, nullable=False)
    session_id = Column(String, nullable=False)
    journey_id = Column(String, nullable=False)
    current_url = Column(String, nullable=False)
    host = Column(String, nullable=False)
    pathname = Column(String, nullable=False)
    browser = Column(String, nullable=False)
    device = Column(String, nullable=False)
    screen_height = Column(Integer, nullable=False)
    screen_width = Column(Integer, nullable=False)
    event_type = Column(String, nullable=False)
    element_type = Column(String, nullable=False)
    element_text = Column(Text, nullable=True)
    timestamp = Column(String, nullable=False)
    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)
    mouse_button = Column(Integer, nullable=False)
    ctrl_key = Column(Boolean, nullable=False)
    shift_key = Column(Boolean, nullable=False)
    alt_key = Column(Boolean, nullable=False)
    meta_key = Column(Boolean, nullable=False)

    element_attributes = relationship(ElementAttributeModel, back_populates="event")

