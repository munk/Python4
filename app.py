from flask import Flask
import json
import sqlite3

app = Flask(__name__)
db = sqlite3.connect('noms.db', check_same_thread=False)

def query(zipcode):
    q = "SELECT * FROM NEIGHBORHOOD WHERE ZIPCODE = ?"
    cur = db.cursor()
    cur.execute(q, [zipcode])
    result = cur.fetchone()
    try:
        return {'zipcode': result[0], 'grade': result[1], 'rating': result[2]}
    except:
        return {'error': 'Unable to find zipcode %s' % zipcode}

def all_zipcodes():
    q = "SELECT ZIPCODE FROM NEIGHBORHOOD"
    cur = db.cursor()
    cur.execute(q)
    return [code[0] for code in cur.fetchall()]

@app.route("/")
def home():
    return json.dumps(all_zipcodes())


@app.route("/<zipcode>")
def zipdata(zipcode):
    response = query(zipcode)
    return json.dumps(response)

if __name__ == '__main__':
    app.run(debug=True)
