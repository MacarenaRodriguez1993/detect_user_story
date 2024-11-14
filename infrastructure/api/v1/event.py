from fastapi import APIRouter, Depends, HTTPException, Query
from application.interfaces import EventPayload
from application.use_cases.get_event_use_case import GetEventUseCase
from application.use_cases.save_event_use_case import SaveEventUseCase
from infrastructure.dependences.event_dependence import get_get_event_use_case, get_save_event_use_case

router = APIRouter()

@router.post("/events")
async def save_events(
    event_payload:EventPayload,
    use_case:SaveEventUseCase=Depends(get_save_event_use_case)
    ):
    try:
        return await use_case.execute(event_payload.events)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
    
@router.get("/stories")
async def get_stories(
    session_id:str=Query(None),
    use_case:GetEventUseCase=Depends(get_get_event_use_case)
):
    try:
        return await use_case.execute(session_id)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))


@router.get("/tests")
async def get_tests():
    print('test')
