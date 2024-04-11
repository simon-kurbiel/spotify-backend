from flask import Flask
from .routes import user, auth
app = Flask(__name__)

app.register_blueprint(user.router, url_prefix="/api/user")
app.register_blueprint(auth.router)

@app.route('/api')
def home():
    return {"message": "Welcome to SpotiDance API"}

