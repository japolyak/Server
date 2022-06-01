from functools import wraps
from flask import Blueprint, jsonify, request
from errors import APIError
from hashlib import pbkdf2_hmac

import os
import db
import secrets
import jwt

bp = Blueprint("auth", __name__)

secret = os.getenv('SECRET', 'default')


@bp.route("/registration", methods=['POST'])
def registration():
    regist = request.get_json()
    pass_word = regist["password"]
    salt = secrets.token_hex(16)

    hs = pbkdf2_hmac('sha256', pass_word.encode(), salt.encode(), 500_000)
    hs = hs.hex()

    conn = db.get_db()
    cur = conn.cursor()
    cur.execute("insert into auth (login, hash, salt) values (?, ?, ?)", (regist["login"], hs, salt))
    cur.execute("insert into people (login) values (?)", (regist["login"], ))
    conn.commit()

    a = {}
    return jsonify(a)


@bp.route("/login", methods=['POST'])
def login():
    login_in = request.get_json()
    name = login_in["login"]

    conn = db.get_db()
    cur = conn.cursor()
    cur.execute("select login, hash, salt from auth where `login` = ?", (name,))
    check = cur.next()

    if check is None:
        raise APIError(404, 'The user with this login doesn\'t exist, please register')

    pass_word = login_in["password"]

    hs = pbkdf2_hmac('sha256', pass_word.encode(), check[2].encode(), 500_000)
    equal = hs.hex()

    if equal != check[1]:
        raise APIError(404, 'The password is incorrect')

    payload = {
        'login': name
    }

    encoded = jwt.encode(payload, secret, algorithm="HS256")

    a = {
        'token': encoded
    }
    return a


@bp.route("/secret")
def sekret():
    token = request.args.get("token")

    try:
        name = jwt.decode(token, secret, algorithms="HS256")
    except jwt.exceptions.DecodeError:
        raise APIError(401, 'Invalid token')

    return jsonify(name)


def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        auth_header = request.headers.get('authorization')  # Bearer ojnpiu9sadhf0789123n4
        token = auth_header.split()[1]

        try:
            payload = jwt.decode(token, secret, algorithms="HS256")
        except jwt.exceptions.DecodeError:
            raise APIError(401, 'Invalid token')

        res = f(*args, **kwargs, token_payload=payload)
        return res

    return wrapped
