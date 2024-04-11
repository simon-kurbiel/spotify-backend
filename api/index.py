from flask import Flask

app = Flask(__name__)

@app.route('/api')
def home():
    return {"message": "Welcome to SpotiDance API"}

