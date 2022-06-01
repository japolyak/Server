from flask import g

import mariadb
import sys
import os


def get_db():
    if 'db' not in g:
        try:
            print('Connected to DB')
            g.db = mariadb.connect(
                user = os.getenv('APP_DB_USER', 'default'),
                password = os.getenv('APP_DB_PASS', 'default'),
                host = os.getenv('APP_DB_HOST', 'default'),
                port = int(os.getenv('APP_DB_PORT', 'default')),
                database = os.getenv('APP_DB_DB', 'default')
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    return g.db


def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS people
        (
            id    INT AUTO_INCREMENT,
            name  text null,
            sname text null,
            login text null,
            PRIMARY KEY (id)
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS mems
        (
            id    INT AUTO_INCREMENT,
            name  TEXT,
            link TEXT,
            person_id INT,
            PRIMARY KEY (id)
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS auth
        (
            login  varchar(32),
            hash TEXT,
            salt TEXT,
            PRIMARY KEY (login)
        );
    """)
    cur.close()



