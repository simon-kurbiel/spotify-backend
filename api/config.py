from pydantic_settings import BaseSettings
import os



class Settings(BaseSettings):
    SECRET_KEY:str= os.environ.get("SECRET_KEY")
    REDIRECT_URI:str=os.environ.get("CLIENT_ID")
    CLIENT_ID:str=os.environ.get("REDIRECT_URI")
    CLIENT_SECRET:str=os.environ.get("CLIENT_SECRET")
    SPOTIFY_AUTH_URL:str = "https://accounts.spotify.com/authorize"
    STATE_VALUE:str =os.environ.get("STATE_VALUE")
    BACKEND_URL:str=os.environ.get("BACKEND_URL")
        
settings = Settings()