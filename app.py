from flask import Flask, render_template, request
import socket
import os

app = Flask(__name__)


# Get environment variables, or set defaults
background_color    = os.environ.get('BACKGROUND_COLOR', '#a8d1df ')
custom_text         = os.environ.get('CUSTOM_TEXT', 'Hello World!')
text_color          = os.environ.get('TEXT_COLOR', 'black')
title               = os.environ.get('APP_NAME', 'Dockerized Flask App')
version             = os.environ.get('APP_VERSION', 'v1.0.0')


@app.route("/")
def hello_world():
    # Get the hostname of the container
    hostname = socket.gethostname()
    # Renders templates/index.html with the variables
    return render_template('index.html', 
                            title=title,
                            custom_text=custom_text,
                            version=version,
                            hostname=hostname,
                            background_color=background_color, 
                            text_color=text_color)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=3000)