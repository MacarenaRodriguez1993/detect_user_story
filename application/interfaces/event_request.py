from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class ElementAttributes(BaseModel):
    class_element:  Optional[str] = Field(None, alias='class')
    href: Optional[str]=None
    extra_attributes: Dict[str, Any] = {}

class EventProperties(BaseModel):
    distinct_id: str
    session_id: str
    journey_id: str
    current_url: str = Field(..., alias='$current_url')  
    host: str = Field(..., alias='$host')                
    pathname: str = Field(..., alias='$pathname')        
    browser: str = Field(..., alias='$browser')          
    device: str = Field(..., alias='$device')
    screen_height: int = Field(..., alias='$screen_height')
    screen_width: int = Field(..., alias='$screen_width')  
    eventType: str
    elementType: str
    elementText: str
    elementAttributes: dict
    timestamp: str
    x: int
    y: int
    mouseButton: int
    ctrlKey: bool
    shiftKey: bool
    altKey: bool
    metaKey: bool

    referrer: Optional[str] = Field(..., alias='$referrer')
    referring_domain: Optional[str] = Field(..., alias='$referring_domain')

class Event(BaseModel):
    event: str
    properties: EventProperties
    timestamp: str

class EventPayload(BaseModel):
    events:List[Event]