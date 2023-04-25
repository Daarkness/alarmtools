
#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json


class Http:

    def post(self,headers:dict,url:str,json_text:dict ):
        return requests.post(url ,json.dumps(json_text),headers=headers).content


class WechatHttp(Http):
    def send_msg(self,alarm_msg:str,web_hook:str):
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        json_text = {
            "msgtype": "markdown",
                "markdown": {
                    "content": alarm_msg
                },
            }
        reuslt = super().post(headers = headers,url=web_hook,json_text=json_text)
        return reuslt
