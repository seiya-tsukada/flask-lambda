# coding: utf-8

from jinja2 import Environment, FileSystemLoader
import os

def lambda_handler(event, context):

    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"), encoding="utf8"))
    template = env.get_template("index.html")

    var = "world"
    params = event["params"]

    html = template.render(var=var, params=params)

    return  html