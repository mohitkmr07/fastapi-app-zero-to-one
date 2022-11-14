import logging

import uvicorn
from fastapi import FastAPI

from app.api.endpoints.v1 import router
from app.common.api_exceptions import RequestErrorHandler, RequestError
from app.core.cache.redis_cache import initialize_cache
from app.core.db.db_session import engine
from app.database.postgres.model import model
from app.middleware.request_middleware import RequestContextLogMiddleware

app = FastAPI()

model.metadata.create_all(bind=engine)
app.include_router(router.api_router, prefix='/v1')
app.add_middleware(RequestContextLogMiddleware)


@app.exception_handler(RequestError)
async def request_error_internal(request, exc):
    reh = RequestErrorHandler(exc=exc)
    return reh.process_message()


@app.on_event("startup")
async def initialize():
    await initialize_cache()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001, proxy_headers=True, forwarded_allow_ips="*",
                use_colors=True, env_file="dev.env")
