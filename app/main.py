from fastapi import FastAPI, HTTPException, Depends
from . import models
from .database import engine
from .routers import routes_router
from .data_loader import load_data


app = FastAPI()

app.include_router(routes_router)

@app.on_event("startup")
def startup_event():
    models.Base.metadata.create_all(bind=engine)
    load_data('/app/web_challenge.csv')
@app.get("/")
async def root():
    return {"message": "Hello World"}

