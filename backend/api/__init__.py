from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from backend import config

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.FRONTEND_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def status():
    return {"status": "up"}


@app.exception_handler(500)
async def internal_server_error_handler(request, exc):
    return JSONResponse(
        {"detail": "Something went wrong! We are looking into it."}, status_code=500
    )
