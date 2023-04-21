from flask import Flask, render_template
from helper import *

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/hello-world")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/')
def homepage():
	test = HITHERE('HIIIII')
	return render_template('index.html', data=test) # data is what you use to call this object in the html

@app.route('/fname')
def fname():	
	return render_template('fname.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)

# flask --app flask_html.py --debug run
# bonus points if you can start this as a service on windows to run
# serving it on a Linux device so you can access it on your LAN is even cooler
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04