from flask import Flask
app = Flask(__name__)

# Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'
    
export; FLASK_APP = app.py
set; FLASK_APP = app.py