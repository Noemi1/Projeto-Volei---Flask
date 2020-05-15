from flask import Flask, g
from db import query_db, get_db

app = Flask(_name_)

app.app_context().push()

@app.before_request
def before_request():
    g.db = get_db()
    g.query_db = query_db
    print(g.db)
    print(g.query_db)

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


from controller import *

if _name_ == "_main_":
    app.run(debug=True)