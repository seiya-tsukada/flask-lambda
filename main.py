# coding: utf-8

from jinja2 import Environment, FileSystemLoader
import os

def lambda_handler(event, context):

    print os.path.join(os.path.dirname(__file__), 'templates')

    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'), encoding='utf8'))

    template = env.get_template('index.html')
    html = template.render()

    return {
      "statusCode": 200,
      "headers": {"Content-Type": "text/html"},
      "body": html
    }