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


def get_new_track(order_response):
    return order_response.json().get("track")


data.params_get["t"] = get_new_track(order_response)


def positive_assert():
    track_response = get_order(data.params_get)
    assert track_response.status_code == 200


def test_get_order_by_track_success():
    positive_assert()
