from flask import Flask, g
from db import query_db, get_db

app = Flask(__name__)

app.app_context().push()

@app.before_request
def before_request():
    g.db = get_db()
    g.query_db = query_db

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


from controller import *

if __name__ == "__main__":
    app.run(debug=True)