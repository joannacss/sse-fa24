# An example of a 
# To run: flask --app hello_world  --debug run
# (The --debug will allow auto reload)

from flask import Flask
from flask import render_template, make_response



app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hello.html", name="SSE Fall 2023!")

