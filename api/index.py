from flask import Flask, jsonify
from .routes import user, auth
from .config import settings
from .utils.enums import StatusCodes
app = Flask(__name__)


app.secret_key = settings.SECRET_KEY
app.register_blueprint(user.router, url_prefix="/api/user")
app.register_blueprint(auth.router, url_prefix = "/api/")

@app.route('/api/hello')
def home():
    return {"message": "Welcome to SpotiDance API"}, 200

@app.errorhandler(404)
def not_found_error(error):
    return {"success":False, "message": "endpoint does not exist"},StatusCodes.PAGE_NOT_FOUND.value

