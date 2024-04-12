import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from cleanflask.db import get_db

# router for blueprint
blueprint_url = 'blueprint'
bp = Blueprint(blueprint_url, __name__, url_prefix=f'/{blueprint_url}') 


@bp.before_app_request
def todo_befor_app_request():
    # todo
    user_id = session.get('user_id')

    g.user = user_id
    
    g.whatever = "fill something you want by adding params of g"

# BaseURL/blueprint
@bp.route('/')
def blue_root():
    return (
        "there is blueprint"
    )

# GET BaseURL/blueprint/register
@bp.route('/bluehello', methods=('GET',)) 
def blue_hello():
    return({
        "user_id": g.user,
        "msg": "hello, this is blueprint",
        "whatever": g.whatever
    })
    
