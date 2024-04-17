from flask import session, request, redirect, url_for
from functools import wraps
from .enums import StatusCodes, Status
import requests
from ..config import settings

def check_token_validity(access_token:str):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    res = requests.get('https://api.spotify.com/v1/me', headers=headers)
   
    if res.status_code == StatusCodes.OK.value:
      
        return Status.SUCCESS
    return Status.FAILURE
   
def check_refresh_token_validity(refresh_token:str):
    token_url = 'https://accounts.spotify.com/api/token'
    data = {
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token,
                'client_id': settings.CLIENT_ID,
                'client_secret': settings.CLIENT_SECRET
    }
    res = requests.post(token_url, data=data)
    if res.status_code == StatusCodes.OK.value:
                
        access_token = res.json()["access_token"]
        session["access_token"] = access_token
        return Status.SUCCESS
    return Status.FAILURE
   

def token_required_exclude(exclude_routes):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Check if the current route is in the exclude list
            if request.endpoint in exclude_routes:
                return f(*args, **kwargs)
            # If not excluded, apply token_required decorator
            access_token, refresh_token = session.get("access_token"), session.get("refresh_token")
            if access_token is None and refresh_token is None:
                return redirect(url_for("auth.login"))
                return {'success': False, 'message': "Unauthenticated"}, 401
            elif access_token:
                token_status = check_token_validity(access_token)
                if token_status == Status.FAILURE:
                    return {'success': False, 'message': "Unauthenticated"}, 401
            else:
                refresh_token_status = check_refresh_token_validity(refresh_token)
                if refresh_token_status == Status.FAILURE:
                    return {'success': False, 'message': "Unauthenticated"}, 401
            return f(*args, **kwargs)
        return decorated_function
    return decorator
    