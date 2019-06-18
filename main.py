#https://becominghuman.ai/full-stack-web-development-python-flask-javascript-jquery-bootstrap-802dd7d43053
#https://testdriven.io/blog/adding-a-custom-stripe-checkout-to-a-flask-app/
#https://www.tutorialspoint.com/flask/flask_templates.htm
#https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications
#https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
#test out GoCD
#https://docs.sqlalchemy.org/en/13/orm/session_basics.html
#https://realpython.com/python-web-applications-with-flask-part-ii/
#https://pusher.com/tutorials/live-table-flask
"""This is the routing file - all pages of website will be directed from here"""
from application import create_app, cli

# Create the flask application
flask_app = create_app()

# Register custom CLI commands
cli.register(flask_app)

if __name__ == "__main__":
    flask_app.run(host='127.0.0.1', port=80)

"""
import stripe

from flask import Flask, render_template, jsonify, flash, redirect
from datetime import datetime

flask_app = Flask(__name__)

#from app import routes


#Routing for the home page
@flask_app.route("/")
def index():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d, %B, %Y at %X")
    content = "Hello, the time is " + formatted_now
    return render_template('index.html', key=formatted_now)


#Routing for the registration page
@flask_app.route("/register")
def register():
    return "Registration"


#Routing for the blog redirect
@flask_app.route("/blog")
def blog():
    return redirect("https://blog.orientation.skule.ca/")


#Routing for the FAQ page
@flask_app.route("/faq")
def faq():
    return "FAQ Page"


#Routing for the Events and Schedule page
@flask_app.route("/schedule")
def schedule():
    content = "this c'est un test"
    return content


#This runs the app when the file is run using 'python app.py' instead of having to run it using 'flask run
if __name__ == "__main__":
    flask_app.run()

#If want to pass in variables from the URL into the function
#@app.route('/meanreversion/result/<security>/<start_date>/<end_date>/<int:sma_>/<int:lma_>')
#def meanreversion_result(security,start_date,end_date,sma_,lma_):


"""
