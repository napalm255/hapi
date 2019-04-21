#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Halo API.
"""

from chalice import Chalice
from chalicelib.tips import random_tip, all_tips

app = Chalice(app_name='hapi')  # pylint: disable=invalid-name

METHODS = ['POST']

@app.route('/', methods=METHODS)
def index():
    """Return available commands."""
    commands = ['!tips']
    cmds = ''.join(['* {}\n'.format(c) for c in commands])
    msg = ("**Available Commands:**\n"
           "{0}\n").format(cmds)
    return {'message': msg, 'commands': commands}

@app.route('/tips', methods=METHODS)
def get_random_tip():
    """Return random tip."""
    return {'message': random_tip()}

@app.route('/tips/all', methods=METHODS)
def get_all_tips():
    """Return all tips."""
    tips = all_tips()
    response = {'message': '\n'.join(tips),
                'tips': tips}
    return response

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
