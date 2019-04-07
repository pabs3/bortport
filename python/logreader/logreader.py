from flask import Flask
from flask import render_template
from flask import request

import sqlite3

app = Flask(__name__)

get_sessions_sql = """
SELECT session,min(timestamp) AS time 
FROM midi 
GROUP BY session 
ORDER BY timestamp DESC
"""

get_midis_sql = """
SELECT rowid,* from midi 
WHERE session = ?
ORDER BY timestamp
"""

annotate_sql = """
UPDATE midi
SET notes = ?
WHERE rowid = ?
"""

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route("/")
def sessions():
    conn = sqlite3.connect("logs.db")
    conn.row_factory = dict_factory
    c = conn.cursor()
    r = c.execute(get_sessions_sql) #.fetchall()
    return render_template('sessionlist.html',sessions=r)

@app.route('/session/<sessionid>')
def session(sessionid):
    print (sessionid)
    conn = sqlite3.connect("logs.db")
    conn.row_factory = dict_factory
    c = conn.cursor()
    r = c.execute(get_midis_sql,[sessionid]) #.fetchall()
    return render_template('loglist.html',messages=r)

@app.route('/annotate/<id>',methods=['POST'])
def annotate(id):
    data = request.form['data']
    conn = sqlite3.connect("logs.db")
    conn.row_factory = dict_factory
    c = conn.cursor()
    r = c.execute(annotate_sql,[data,id])
    conn.commit()
    return "{'OK':'OK'}"