from flask import Flask
import os
from flask import jsonify


app = Flask(__name__)

my_name = "Natalie"
host_name = os.environ.get("HOSTNAME")


@app.route("/")
def hello_world():
    return "Hello, World " + my_name + " !"


@app.route("/hostname")
def hostname():
    return jsonify({"hostname": host_name})


@app.route("/host")
def kubernetes_env_variables():
    return "Hello, World!"
