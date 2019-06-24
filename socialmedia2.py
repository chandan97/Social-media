import sqlite3 as sql
from os import path


ROOT = path.dirname(path.relpath((_file_)))


def  post_create(name,content):

    con = sql.connector(path.join(ROOT,'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name,contents) values(?,?',(name,content))
    con.commit()
    con.close()


def get_newposts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts
