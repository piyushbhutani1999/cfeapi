import requests #allows yout to do http request
import json
BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"


def get_list():

    r  = requests.get(BASE_URL + ENDPOINT)

    # print(r.status_code) --> 200
    # by determing the type of status code diff types of CRUP operations are assumed
    # 404 --> page not found
    # status_code.ok
    
    #  print("r : ", r) --> ('r : ', <Response [200]>)
    #  response 200 is for get request.

    #  The type of the return value of .json() is a dictionary,
    #  so you can access values in the object by key.

    # print(r.json) -> [
    #    {u'content': u'updates 1', u'user': 1}, 
    #    {u'content': u'updates 2', u'user': 1},
    #    {u'content': u'updates 3', u'user': 1}
    # ]

    # print(type(r.json())) --> list(as it is a python list)

    # print(type(json.dumps(r.json))) --> string(as it is json format)

    return r.json()

print(get_list())
