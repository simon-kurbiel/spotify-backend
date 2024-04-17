from flask import Blueprint, request, session, redirect, url_for
import requests
from ..config import settings
from ..utils.enums import StatusCodes, Status
from ..utils.helpers import token_required_exclude
router = Blueprint("auth", __name__)

@router.before_request
@token_required_exclude(["auth.login", "auth.logout", "auth.callback"])
def apply_token_required():
    pass

@router.get("/docs")
def get_docs():
    return {
        "logout":f'{settings.BACKEND_URL}logout',
        "playlists": f'{settings.BACKEND_URL}playlists'
    }
@router.get("/login")
def login():
    """Login to spotify account"""
    
    spotify_auth_url = settings.SPOTIFY_AUTH_URL
    params = {
        'client_id': settings.CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': settings.REDIRECT_URI,
        'scope': 'user-read-private user-read-email',  # Add scopes as needed
        # Optional state parameter for security
        'state': settings.STATE_VALUE
    }
    auth_url = '{}?{}'.format(spotify_auth_url, '&'.join(['{}={}'.format(k, v) for k, v in params.items()]))
    
    return redirect(auth_url)



@router.get("/callback")
def callback():
    
    code = request.args.get('code')
    state = request.args.get('state')
    
    if code:
        token_url:str = 'https://accounts.spotify.com/api/token'
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': settings.REDIRECT_URI,
            'client_id': settings.CLIENT_ID,
            'client_secret': settings.CLIENT_SECRET
        }
        res = requests.post(token_url, data=data)
        if res.status_code == StatusCodes.OK.value:
            access_token,refresh_token = res.json()["access_token"], res.json()["refresh_token"]
            session["access_token"] = access_token
            session["refresh_token"] = refresh_token
            return redirect(url_for("auth.get_docs"))
            return {"success":True,"access_token": access_token}, StatusCodes.OK.value
    
        
    return {"success":False, "message": "Unauthenticated"}, StatusCodes.UNAUTHORIZED.value


    
@router.get("/logout")
def logout():
    session.pop('access_token',None)
    session.pop('refresh_token',None)
    
    return {"success":True}, StatusCodes.OK.value



@router.get("/profile")
def get_profile():
    access_token = session.get("access_token")
    if access_token:
        headers = {
            "Authorization":f'Bearer {access_token}'
        }
        res = requests.get("https://api.spotify.com/v1/me", headers=headers)
       
        if res.status_code == StatusCodes.OK.value:
            
            return {"profile":res.json()}
    return {"profile":False}

@router.get("/playlists")
def get_playlists():
    return {"playlists": {}}



