

import abc

import jinja2 
import datetime as datetime_S
from datetime import datetime

__ALARM_DICT__ = {
    "0":"信息",
    "1":"警告",
    "2":"一般严重",
    "3":"严重",
    "4":"灾难"
} 
class Template(abc.ABC):
 
    @abc.abstractmethod
    def mapping(self,tmplate:str,mip:dict):
        pass

class WechatTemplate(Template):

    def __init__(self,tmplate:str) -> None:
        self.tmplate = tmplate
    
    def mapping(self,data_dict: dict)->str:
        print(data_dict)
 
        tmp = jinja2.Template(self.tmplate)
        changed_str = tmp.render(seq=data_dict) 
        return  changed_str 



def _datetimeformat(value): 
    date_s = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S:%fZ')

    out_date = (date_s + datetime_S.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

    return out_date    

def _datetimeformat_t(value): 
    try: 
    	date_s = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError as e:
        date_s = datetime.strptime(value,'%Y-%m-%dT%H:%M:%SZ')
    out_date = (date_s + datetime_S.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    return out_date    

def _alarmlevelformat(value):
    return __ALARM_DICT__[value]

jinja2.filters.FILTERS['datetimeformat'] = _datetimeformat
jinja2.filters.FILTERS['datetimeformat_t'] = _datetimeformat_t
jinja2.filters.FILTERS['alarmlevelformat'] = _alarmlevelformat


wechat_tmplate_str = """
{% if seq[0].status == "resolved" %}
[Prometheus恢复信息]({{ seq[0].generatorURL }})
{% for res in seq %}
>**[{{ res.labels.alertname}}]({{ res.generatorURL }})**
><font color=\"info\"> 告警级别</font>: {{ res.labels.level|alarmlevelformat }}
><font color=\"info\"> 开始时间</font>: {{ res.startsAt|datetimeformat_t }}
><font color=\"info\"> 结束时间</font>: {{ res.endsAt|datetimeformat_t }}
><font color=\"info\"> 故障主机IP</font>: {{ res.labels.name }}
>**<font color=\"info\"> 故障描述 {{ res.annotations.description }}</font>**
{% endfor %}
{% else %}
[Prometheus告警信息]({{ seq[0].generatorURL }})
{% for res in seq %}
>**[{{ res.labels.alertname}}]({{ res.generatorURL }})**
><font color=\"warning\"> 告警级别</font>: {{ res.labels.level|alarmlevelformat }}
><font color=\"warning\"> 开始时间</font>: {{ res.startsAt|datetimeformat_t }}
><font color=\"warning\"> 故障主机IP</font>: {{ res.labels.name }}
>**<font color=\"warning\"> 故障描述 {{ res.annotations.description }}</font>**
{% endfor %}
{% endif %}
"""


wechatalarm_tmp = WechatTemplate(wechat_tmplate_str)

