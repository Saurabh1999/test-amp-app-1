from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=int(os.environ["CDSW_READONLY_PORT"]))


