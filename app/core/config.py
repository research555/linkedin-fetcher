import secrets
from pydantic_settings import BaseSettings

class Settings(BaseSettings):


    # # # # PROXYCURL # # # #
    PROXYCURL_API_KEY: str

    # # # # FASTAPI # # # #
    PROJECT_NAME: str
    PROJECT_V1_NAME: str

    # # # # ENV # # # #
    DEBUG: bool = True

    # # # # GOOGLE CLOUD STORAGE # # # #
    GCP_SERVICE_ACCOUNT_KEY_POINTER: str
    BUCKET_RELATIVE_FILE_PATH: str
    BUCKET_NAME: str
    GCP_PROJECT_ID_PRODUCTION: str
    GCP_PROJECT_ID_STAGING: str



    # CORS
    ALLOW_ORIGINS: list = ["*"]
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: list = ["*"]
    ALLOW_HEADERS: list = ["*"]

    class Config:

        env_file = ".env"


settings = Settings()
