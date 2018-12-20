#! /bin/env python
# coding: utf-8

from flask import Blueprint, render_template, request, redirect, url_for
import os, commands, json
import pprint

main = Blueprint("main", __name__)

@main.route("/")
def index():

  return "hello world"
  # return render_template("index.html", var="world")
