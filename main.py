# coding: utf-8

from jinja2 import Environment, FileSystemLoader
import path

def lambda_handler(event, context):

  env = Environment(loader=FileSystemLoader(path.join(path.dirname(__file__), 'templates'), encoding='utf8'))
  
  template = env.get_template('index.html')
  html = template.render()
  
  return {
      "statusCode": 200,
      "headers": {"Content-Type": "text/html"},
      "body": html
  }