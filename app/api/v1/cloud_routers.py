from typing import List, Optional, Dict
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
import app.utils as utils
import app.schemas as schemas

from typing import Any, Dict, List, Union
import json
from fastapi import APIRouter, HTTPException, status
from app import schemas
from app.services.external_services import gcs


router = APIRouter()

@router.post(path="/upload/",
             status_code=status.HTTP_201_CREATED,
             response_model=schemas.UploadToCloudResponse)
async def upload_to_cloud(
        data: Union[Dict[str, Any], List[Dict[str, Any]]],
        base_folder: str,
        sub_folder: str,
        filename: str,
        ):  # FIXME: Kinda hard to make a request model for this so i left it for later
    """
    Upload linkedin profile data using a linkedin url
    """
    data = json.dumps(data, indent=4)
    try:
        blob_path = gcs.upload_blob(
                                base_folder=base_folder,
                                subfolder=sub_folder,
                                filename=filename,
                                data=data,
                            )
        return schemas.UploadToCloudResponse(blob_path=blob_path)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error uploading to cloud: {e}")


@router.get(path="/download/", status_code=status.HTTP_200_OK)
async def download_from_cloud(
        base_folder: str,
        sub_folder: str,
        filename: str
):

    """
    Download linkedin profile data using a linkedin url
    """
    try:
        data = gcs.retrieve_blob_data(base_folder=base_folder,
                                      subfolder=sub_folder,
                                      filename=filename)
        if data:
            return data
        return None
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error downloading from cloud: {e}")