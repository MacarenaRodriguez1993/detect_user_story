from typing import List, Optional
from pydantic import BaseModel

class Actions(BaseModel):
    type:str
    target:Optional[str]
    value:Optional[str]
    
class UserHistory(BaseModel):
    title:str
    actions:List[Actions]