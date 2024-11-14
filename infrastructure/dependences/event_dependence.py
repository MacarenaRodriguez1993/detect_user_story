from fastapi import Depends
from sqlalchemy.orm import Session
from application.use_cases.get_event_use_case import GetEventUseCase
from data_base_config import get_db

from application.use_cases.save_event_use_case import SaveEventUseCase
from domain.repository.event_repository import EventRepository
from domain.services.get_event_service import GetEventService
from domain.services.save_event_service import SaveEventService
from infrastructure.adapters.postgres.event_repository import PostgresEventRepository

def get_get_event_repository(engine: Session = Depends(get_db))->EventRepository:
    return PostgresEventRepository(engine)


def get_save_service(
    repositpry:EventRepository=Depends(get_get_event_repository)
)->SaveEventService:
    return SaveEventService(repositpry)

def get_get_service(
    repositpry:EventRepository=Depends(get_get_event_repository)
)->GetEventService:
    return GetEventService(repositpry)


def get_save_event_use_case(
    service:SaveEventService=Depends(get_save_service)
)->SaveEventUseCase:
    return SaveEventUseCase(service)

def get_get_event_use_case(
    service:GetEventService=Depends(get_get_service)
)->GetEventUseCase:
    return GetEventUseCase(service)


