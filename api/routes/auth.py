from flask import Blueprint, request, session, redirect
import requests

router = Blueprint("auth", __name__)

@router.get("/login")
def login():
    return {"msg": "login"}

@router.get("/callback", __name__)
def callback():
    return {"message": "callback"}

@router.get("/logout")
def logout():
    return {"message": "logout"}

