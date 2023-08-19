import configuration
import data
import requests

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
           json=data.order_body)

def get_number_new_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO,
           params={"t": track_number})