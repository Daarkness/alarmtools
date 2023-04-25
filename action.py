import abc
from common import httpclient
 

class Action(abc.ABC):
    @abc.abstractmethod
    def do_aticon():
        print ("alarm msg to some where.")

 

class WeChatAlarmAction(Action):

    def __init__(self,web_hooks:list,template:str) -> None:
        self.wechat_alarm_conf = {
            "web_hooks":web_hooks,
        }
        self.template = template


    def alarm(self,data):
        mip_data =self.template.mapping(data )
        http_clint = httpclient.WechatHttp()
        for web_hook in self.wechat_alarm_conf['web_hooks']:
            http_clint.send_msg(alarm_msg=mip_data,web_hook=web_hook)

    def do_aticon(self,data):
        self.alarm(data)



class SilenceAlarmAction(Action):

    def __init__(self) -> None:
        pass 

    def do_aticon(self,data):
        pass

# class TestsPhoneAlarmAction(Action):
#     def __init__(self,web_hooks:str,phone_list:list,tmp:str) -> None:
#         self.wechat_alarm_conf = {
#         "web_hook":str,
#         "phone_list":phone_list,
#     }
#     def do_aticon(self):
#         for phone_num in self.phone_alarm_conf:
#             print("---call...")

# class AddLevelAction(Action):
#     def __init__(self) -> None:
#         pass
#     def do_aticon(self):
#         print('level plus 1 ')
