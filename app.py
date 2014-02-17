from flask import Flask
app = Flask(__name__)

from yelp import phone_search
from inspections import inspection_data

@app.route("/")
def hello():
    return "Hello World!"

def foo():
    data = inspection_data('manhattan', 10)
    for d in data:
        for phone in d[1].PHONE:
            result = phone_search(phone)
            print result.text
            print result.url


if __name__ == "__main__":
    foo()
