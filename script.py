import requests #allows yout to do http request
import json

BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"


def get_list():

    r  = requests.get(BASE_URL + ENDPOINT)

    # print(r.status_code) --> 200
    # by determing the type of status code diff types of CRUP operations are assumed
    # 404 --> page not found
    # requests.codes.ok means the status_code is fine i.e. not givin error
    
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


def create_update():
    new_data = {
        'user' : 1,
        "content" : "newly added object",
    }
    r = requests.post(BASE_URL + ENDPOINT, data = new_data)

    # print(r.status_code) --> 403
    # if r.status_code == request.codes.ok means it is not throwing any errors


    # print(r.json()) -->
    # ERROR because when i comment out post function in
    # apiviews then request is not able to find any post method in this usl
    # so STATUS_CODE = 403 // post method not found

    # CONSOLE :
    # [30/Jan/2020 19:02:33] "POST /api/updates/ HTTP/1.1" 403 2857
    #       Forbidden(CSRF cookie not set.): / api/updates/
    # for posting any thing django wants us to sign in
    # thats why CFRS token error is throwing
    # now we use method CFRSEXEMPT to let django enter me without any verification
    # but make sure that you will remove this after checking

    # print(r.json())
    # print(r.headers) --> give info about which method are allowed ex: get,
    # print(r.text) --> return html page



    # print(r.json()) --> post method is calling now after defining csrf_exempt
    # {u'message': u'i am newly created'}
    

create_update()
