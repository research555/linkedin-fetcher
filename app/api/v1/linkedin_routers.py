from typing import List, Optional, Dict
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
import app.utils as utils
import app.schemas as schemas
from app.services.external_services import proxycurl_api_client

router = APIRouter()


@router.post("/fetch-profiles/",
             status_code=status.HTTP_201_CREATED,
             response_model=schemas.GetLinkedinProfilesResponse
                )
async def fetch_profiles(request: schemas.GetLinkedinProfilesRequest) -> schemas.GetLinkedinProfilesResponse: #FIXME: Redo this piece of shit

    """
    Fetch LinkedIn profiles from a list of urls
    """

    urls = [utils.linkedin_utils.generate_url(url, profile=True) for url in request.linkedin_urls]
    profiles = await proxycurl_api_client.get_bulk_profiles(urls=urls)
    profiles = [profile.value for profile in profiles if profile.error is None]
    return schemas.GetLinkedinProfilesResponse(profiles=profiles)





