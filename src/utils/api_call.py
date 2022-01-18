import requests


def make_get_api_call(url, params=None):
    response = None
    try:
        params = params or dict()
        http_response_object = requests.get(url=url, params=params)
        response = http_response_object.json()
    except Exception as err:
        print("Error Occurred during http call: ", str(err), " INPUT-URL: ", url)
    return response
