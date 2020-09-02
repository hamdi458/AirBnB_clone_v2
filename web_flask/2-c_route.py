#!/usr/bin/python3
"""flaskbzhamd"""
from flask import Flask


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/", strict_slashes=False)
    def hello():
        """'Hello HBNB!'"""
        return "Hello HBNB!"

    @app.route("/hbnb", strict_slashes=False)
    def hbnb():
        """'HBNB'"""
        return "HBNB"

    @app.route("/c/<text>", strict_slashes=False)
    def cs(txt):
        """txt"""
        return 'C ' + txt.replace('_', ' ')
    app.run(host="0.0.0.0", port=5000)
