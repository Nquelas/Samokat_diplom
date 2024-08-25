import configuration

import requests

import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)


order_response = post_new_order(data.order_body)


def get_order(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params=track_order)
