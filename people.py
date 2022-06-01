from flask import Blueprint, request, jsonify
from errors import APIError
from auth import login_required

import os
import db

bp = Blueprint("people", __name__)

people = []
secret = os.getenv('SECRET', 'default')


@bp.route("/people")
def show():
    conn = db.get_db()
    cur = conn.cursor()

    offset = request.args.get('offset')
    limit = request.args.get('limit')

    cur.execute("Select id, name, sname from people order by id limit ?, ?", (offset, limit))

    peop = []

    for (id_p, name, sname) in cur:
        a = {
            'id': id_p,
            'name': name,
            'sname': sname
        }
        peop.append(a)
    return jsonify(peop)


@bp.route("/people", methods=['POST'])
def data_many():
    humans = request.get_json()

    conn = db.get_db()
    cur = conn.cursor()
    added = []

    for h in humans:
        cur.execute("insert into people (name, sname) values (?, ?)", (h['name'], h['sname']))
        add = {
                "id": cur.lastrowid,
                "name": h['name'],
                "sname": h['sname']
        }
        print(add)
        added.append(add)

    conn.commit()

    return jsonify(added)


@bp.route("/people/<human_id>")
def show_by_id(human_id):

    try:
        by_id = int(human_id)
        if by_id < 0:
            raise APIError(404, 'The positive number is required')
    except ValueError:
        raise APIError(405, 'Numbers are required')

    conn = db.get_db()
    cur = conn.cursor()

    cur.execute("select id, name, sname from people where id = ?;", (by_id, ))

    person = cur.next()

    if person is None:
        raise APIError(404, 'The id doesn\'t exist')

    (id_p, name, sname) = person

    show_person = {
        'id': id_p,
        'name': name,
        'sname': sname
    }

    return jsonify(show_person)


@bp.route("/people/<human_id>", methods=['PUT'])
@login_required
def put_human(human_id, token_payload):
    new_person = request.get_json()
    new = new_person[0]

    try:
        add = int(human_id)
        if add < 0:
            raise APIError(404, 'The positive number is required')
    except ValueError:
        raise APIError(405, 'Numbers are required')

    conn = db.get_db()
    cur = conn.cursor()

    cur.execute("select login from people where id = ?;", (add, ))
    log = cur.next()[0]

    if token_payload['login'] != log:
        raise APIError(403, 'Wrong token')

    cur.execute("select id, name, sname from people where id = ?;", (add, ))

    if cur.next() is None:
        raise APIError(404, 'The id doesn\'t exist')

    cur.execute("""update people
                    set
                        name = ?,
                        sname = ?
                    where
                        id = ?;""", (new['name'], new['sname'], add))
    cur.execute("select id, name, sname from people where id = ?;", (add, ))

    for (id_p, name, sname) in cur:
        show_person = {
            'id': id_p,
            'name': name,
            'sname': sname
        }
    conn.commit()
    return jsonify(show_person)


@bp.route("/people/<human_id>", methods=['DELETE'])
@login_required
def delete_by_id(human_id, token_payload):

    added = {}

    try:
        del_id = int(human_id)
        if del_id <= 0:
            raise APIError(404, 'The positive number is required')
    except ValueError:
        raise APIError(405, 'Numbers are required')

    conn = db.get_db()
    cur = conn.cursor()

    cur.execute("select login from people where id = ?;", (del_id, ))
    login = cur.next()[0]

    if token_payload['login'] != login:
        raise APIError(403, 'You have no permission')

    cur.execute("select id, name, sname from people where id = ?;", (del_id, ))

    if cur.next() is None:
        raise APIError(404, 'The id doesn\'t exist')

    cur.execute(f"delete from people where id = ?;", (del_id, ))

    conn.commit()

    return jsonify(added)


@bp.route("/people/<human_id>/mems")
def show_mem_by_id(human_id):

    try:
        by_id = int(human_id)
        if by_id < 0:
            raise APIError(404, 'The positive number is required')
    except ValueError:
        raise APIError(405, 'Numbers are required')

    conn = db.get_db()
    cur = conn.cursor()

    cur.execute("select id, name, sname from people where id = ?;", (human_id, ))

    if cur.next() is None:
        raise APIError(404, 'The id doesn\'t exist')

    mem_range = []
    cur.execute("select id, name, sname from mems where person_id = ?;", (by_id, ))
    for (id_m, name, link, person_id) in cur:
        mem_i = {
            'id': id_m,
            'name': name,
            'link': link,
            'person_id': person_id
        }
        mem_range.append(mem_i)
    return jsonify(mem_range)

#poszel nachuj_2.0
#komment 1.0
#kiska3