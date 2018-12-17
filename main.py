#! /bin/env python
# coding: utf-8

from flask import Flask
from controller.main import main

app = Flask(__name__)

# To controller
# main contents
app.register_blueprint(main)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="8080", debug=True)
