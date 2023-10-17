from fastapi import APIRouter
from .linkedin_routers import router as router_1
from .cloud_routers import router as router_2

router = APIRouter()

router.include_router(router_1, prefix="/linkedin", tags=["Linkedin Endpoints"])
router.include_router(router_2, prefix="/cloud", tags=["Cloud Endpoints"])
