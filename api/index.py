from flask import Flask
from routes import user
app = Flask(__name__)
app.register_blueprint(user.router, url_prefix="/api/user")

@app.route('/api')
def home():
    return {"message": "Welcome to SpotiDance API"}

