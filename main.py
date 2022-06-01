from flask import Flask, jsonify, g
from werkzeug.exceptions import HTTPException
from errors import APIError

import json
import people
import mems
import auth

import db

app = Flask(__name__)
app.register_blueprint(people.bp)
app.register_blueprint(mems.bp)
app.register_blueprint(auth.bp)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.errorhandler(APIError)
def handle_apierror(error):
    er = {}
    er["type"] = error.status
    er["message"] = error.message
    resp = jsonify(er)
    resp.status_code = error.status

    return resp


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

# https://flask.palletsprojects.com/en/2.1.x/appcontext/
@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()


if __name__ == "__main__":
    with app.app_context():
        db.init_db()
    app.run(host="0.0.0.0")
