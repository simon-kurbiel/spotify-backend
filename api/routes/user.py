from flask import Blueprint

router = Blueprint("user", __name__)

@router.get("/")
def user():
    return {"message": "Hello Router"}