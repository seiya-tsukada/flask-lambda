#! /bin/env python
# coding: utf-8

from flask import Flask
from controller.main import main

def lambda_handler(event, context):

    app = Flask(__name__)

    # To controller
    # main contents
    app.register_blueprint(main)

    if __name__ == "__main__":
      app.run(debug=True)
