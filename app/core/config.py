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



    # CORS
    ALLOW_ORIGINS: list = ["*"]
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: list = ["*"]
    ALLOW_HEADERS: list = ["*"]

    class Config:

        env_file = r"C:\Users\immi\PyCharmProjects\Startups\kale-linkedin-api\.env"


settings = Settings()


