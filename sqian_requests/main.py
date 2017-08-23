# -*- coding:utf-8 -*-

import requests
import json

URL = "https://api.github.com"


def build_uri(endpoint):
    return "/".join([URL, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def simple_requests():
    response = requests.get(build_uri('users/qianshuangyang'))
    print better_print(response.text)


simple_requests()
