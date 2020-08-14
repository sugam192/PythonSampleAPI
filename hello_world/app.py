from flask import Flask

app = Flask(__name__)

@app.route('/') # root address of api or HOME page
def home():
    return "Hello, World!"
app.run(port=5000)