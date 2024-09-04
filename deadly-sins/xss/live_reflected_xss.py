# An example of reflected XSS
# To run: flask --app live_reflected_xss  --debug run
# (The --debug will allow auto reload)

from flask import Flask
from flask import render_template, make_response, request



app = Flask(__name__)

@app.route("/")
def hello_world():
    # TODO: change hello world example to echo back the user's name 
    # passed to it as a request parameter
    return render_template("live_reflected_xss.html", name=request.args.get("name"))
    





