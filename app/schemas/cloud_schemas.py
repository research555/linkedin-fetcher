from pydantic import BaseModel


class UploadToCloudResponse(BaseModel):
    message: str = "File uploaded successfully"
    blob_path: str
