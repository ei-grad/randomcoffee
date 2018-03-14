from os import getenv
import logging

import bottle

from randomcoffee.app import app
from randomcoffee.models import db
from randomcoffee.commands import commands

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')

logger = logging.getLogger(__name__)


@app.route('/')
def home():
    return bottle.redirect(getenv(
        'RANDOMCOFFEE_REDIRECT_URL',
        'https://github.com/ei-grad/randomcoffee'
    ))


@app.route('/' + getenv('WEBHOOK', 'webhook'), method='POST')
def webhook():
    req = bottle.request.json
    if req['message']:
        if req['message']['text'] in commands:
            return commands[req['message']['text']](req)
    else:
        logger.info("Don't know how to handle: %r", req)


@app.hook('after_request')
def rollback():
    db.rollback()
