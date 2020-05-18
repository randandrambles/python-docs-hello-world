from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Domain available for sell. Feel free to contact me at: bilal.khan2014@hotmail.com"
