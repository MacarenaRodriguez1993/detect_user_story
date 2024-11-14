from fastapi import FastAPI
from infrastructure.api.v1 import event_router

from domain.models import element_attribute_model,event_model
from data_base_config import Base,engine

app=FastAPI(
    title="Bugster",
    version="1.0",
    description="Esta api de manejar los eventos de interaccion de los usuarios",
)

Base.metadata.create_all(bind=engine)


app.include_router(event_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)