import logging
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.core import settings
from app.api import router  # Assuming that your router is defined in this module.

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.
    :return: Configured FastAPI application instance.
    """
    application = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)

    # Setup CORS
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOW_ORIGINS,
        allow_credentials=settings.ALLOW_CREDENTIALS,
        allow_methods=settings.ALLOW_METHODS,
        allow_headers=settings.ALLOW_HEADERS,
    )

    # Include routers
    application.include_router(router, prefix=settings.PROJECT_V1_NAME)
    return application


app = create_application()

@app.exception_handler(Exception)
async def validation_exception_handler(request: Request, exc: Exception):
    """
    Handle unexpected exceptions.
    :param request: Incoming request instance.
    :param exc: Exception occurred.
    :return: JSON response with error details.
    """
    logger.error(
        f"An error occurred while processing request {request.method} {request.url}. "
        f"Origin: {request.client.host}. Headers: {request.headers}",
        exc_info=True
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": f"An unexpected error occurred: {exc}"},
    )
