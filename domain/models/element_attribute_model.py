from sqlalchemy import Column, ForeignKey, Integer, String
from data_base_config import Base
from sqlalchemy.orm import relationship

class ElementAttributeModel(Base):
    __tablename__ = "element_attribute"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)

    event_id = Column(Integer, ForeignKey('events.id'))  
    event = relationship("EventModel", back_populates="element_attributes")