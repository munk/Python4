from config import key
from neighborhoods import neighborhoods
from restaurants import restaurants
import requests

_base_url_ = "http://api.yelp.com"


def phone_search(number):
    url = _base_url_ + "/phone_search"
    data = {'phone': number, 'ywsid': key}
    response = requests.get(url, params=data)
    return response

