from flask import Flask, request, make_response
import json


app = Flask(__name__)

@app.route('/show')
def show_cookie():
    cookies = json.dumps(request.cookies)
    return cookies


@app.route('/set')
def set_cookie():
    r = make_response("<b>set cookie</b>")

    r.set_cookie('c1', 'new_value')

    return r


if __name__ == '__main__':
    app.run()