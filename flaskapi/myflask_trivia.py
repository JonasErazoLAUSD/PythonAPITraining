#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)


# This is where we want to redirect users to
@app.route("/success/<name>")
def success(name):
    return f" Great {name}! You answered correctly\n"

# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("trivia_q.html") # look for templates/postmaker.html


# This is where postmaker.html POSTs data to
# A user could also browser (GET) to this location
@app.route("/triviaq", methods = ["POST", "GET"])
def triviaq():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("tanswer"): # if nm was assigned via the POST
            answer = request.form.get("tanswer") # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value defaultuser
            answer = "No answer"
        if request.form.get("nm"):
            user = request.form.get("nm")
        else:
            user = "default_usr"

    # GET would likely come from a user interacting with a browser
    elif request.method == "GET":
        if request.args.get("tanswer"): # if nm was assigned as a parameter=value
            answer = request.args.get("tanswer") # pull nm from localhost:5060/login?nm=larry
        else: # if nm was not passed...
            answer = "no answer" # ...then user is just defaultuser
        if request.args.get("nm"):
            user = request.args.get("nm")
        else:
            user = "default_usr"
    if answer.upper() == 'NEVADA':
        return redirect(url_for("success", name = user)) # pass back to /success with val for name
    else:
        return (redirect(url_for("start")))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
