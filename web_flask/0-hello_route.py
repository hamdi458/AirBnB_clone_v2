#!/usr/bin/python3
"""python3"""
from flask import Flask


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/", strict_slashes=False)
    def hello():
        """that starts a Flask web application"""
        return "Hello HBNB!"
    app.run(host="0.0.0.0", port=5000)
