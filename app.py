from flask import Flask

app = Flask(__name__)

from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def advokaut():
    return "<p>Advokaut.no</p>"

