from fastapi import FastAPI

# from .routers import parser

app = FastAPI()

# app.include_router(parser.router)


@app.get("/health_check")
async def main():
    return {"status": "OK"}
