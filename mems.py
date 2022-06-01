from flask import Blueprint, request, jsonify
from errors import APIError
from auth import login_required

import db
import os

bp = Blueprint("mems", __name__)
secret = os.getenv('SECRET', 'default')
mems = []


@bp.route("/mems")
def show():
    conn = db.get_db()
    cur = conn.cursor()

    offset = request.args.get('offset')
    limit = request.args.get('limit')

    memes = []

    cur.execute("""select
                        mems.id,
                        mems.name,
                        mems.link,
                        mems.person_id,
                        people.name,
                        people.sname
                    from mems
                    join people on mems.person_id = people.id
                    order by mems.id
                    limit ?, ?""", (offset, limit))

    for (mem_id, mem_name, mem_link, mem_person_id, person_name, person_sname) in cur:
        mem_i = {
            'mem_id': mem_id,
            'mem_name': mem_name,
            'mem_link': mem_link,
            'mem_person_id': mem_person_id,
            'person_name': person_name,
            'person_sname': person_sname
        }
        print(mem_i)
        memes.append(mem_i)
    return jsonify(memes)


@bp.route("/mems", methods=['Post'])
@login_required
def data_many(token_payload):
    memes = request.get_json()

    conn = db.get_db()
    cur = conn.cursor()
    added = []

    for m in memes:
        cur.execute("select login from people where id = ?", (m['person_id'], ))
        username = cur.next()[0]

        if token_payload['login'] == username:
            cur.execute("""insert
                            into mems (name, link, person_id)
                            values (?, ?, ?)""", (m['name'], m['link'], m['person_id']))
            add = {
                    "id": cur.lastrowid,
                    "name": m['name'],
                    "link": m['link'],
                    "person_id": m['person_id']
            }
            print(add)
            added.append(add)
            conn.commit()

    return jsonify(added)


@bp.route("/mems/<mem_id>")
def show_mem_by_id(mem_id):
    try:
        by_id = int(mem_id)
        if by_id < 0:
            raise APIError(404, 'The positive number is required')
    except ValueError:
        raise APIError(405, 'Numbers are required')

    conn = db.get_db()
    cur = conn.cursor()

    cur.execute("""select
                        mems.id,
                        mems.name,
                        mems.link,
                        mems.person_id,
                        people.name,
                        people.sname
                    from mems
                    join people on mems.person_id = people.id
                    where mems.id = ?;""", (by_id, ))
    mem = cur.next()

    if mem is None:
        raise APIError(404, 'The id doesn\'t exist')

    (mem_id, mem_name, mem_link, mem_person_id, person_name, person_sname) = mem

    show_mem = {
        'mem_id': mem_id,
        'mem_name': mem_name,
        'mem_link': mem_link,
        'mem_person_id': mem_person_id,
        'person_name': person_name,
        'person_sname': person_sname
    }

    return jsonify(show_mem)


@bp.route("/mems/<mem_id>", methods=['DELETE'])
@login_required
def delete_by_id(mem_id, token_payload):

    added = {}

    try:
        del_id = int(mem_id)
        if del_id <= 0:
            raise APIError(404, 'The positive number is required')
    except ValueError:
        raise APIError(405, 'Numbers are required')

    conn = db.get_db()
    cur = conn.cursor()

    cur.execute("select person_id from mems where id = ?;", (del_id, ))
    person_id = cur.next()[0]

    cur.execute("select login from people where id = ?", (person_id, ))
    person_login = cur.next()[0]

    if token_payload['login'] != person_login:
        raise APIError(403, 'You have no permission')

    cur.execute("select * from mems where id = ?;", (del_id, ))

    if cur.next() is None:
        raise APIError(404, 'The id doesn\'t exist')

    cur.execute("delete from mems where id = ?;", (del_id, ))

    conn.commit()

    return jsonify(added)


@bp.route("/mems/<mem_id>", methods=["Put"])
@login_required
def put_mem(mem_id, token_payload):
    new_mem = request.get_json()
    new = new_mem[0]

    try:
        add = int(mem_id)
        if add <= 0:
            raise APIError(404, 'The positive number is required')
    except ValueError:
        raise APIError(405, 'Numbers are required')

    conn = db.get_db()
    cur = conn.cursor()
    cur.execute("select * from mems where id = ?;", (add, ))
    a = cur.next()

    if a is None:
        raise APIError(404, 'The id doesn\'t exist')

    cur.execute("select login from people where id = ?;", (a[3], ))
    sz = cur.next()[0]

    # Authorization
    if sz != token_payload['login']:
        raise APIError(403, 'You have no permission')

    cur.execute("""update mems
                    set
                        name = ?,
                        link = ?,
                        person_id = ?
                    where
                        id = ?;""", (new['name'], new['link'], a[3], add))
    cur.execute("select id, name, link, person_id from mems where id = ?;", (add, ))

    for (id_p, name, link, person_id) in cur:
        show_mem = {
            'id': id_p,
            'name': name,
            'link': link,
            'person_id': person_id
        }
    conn.commit()
    return jsonify(show_mem)
