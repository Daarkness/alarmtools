
from rules import Rule,Rules
from action import  WeChatAlarmAction,SilenceAlarmAction 
from factor import  defalut_factor,topic_factor,algo_factor
 
from template import  wechatalarm_tmp

wechat_web_hooks = {
    "ops":  ["https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f4ba2ba2-a8cc-4587-b0a5-9246b127c774",],
    "bigdata": ["https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=dd3799ab-e6fe-43f8-b9ff-a4470a4140c1",]
}

 



ops_wechat_actions= [WeChatAlarmAction(wechat_web_hooks["ops"],template=wechatalarm_tmp),]

topic_wechat_actions = [WeChatAlarmAction(wechat_web_hooks["bigdata"],template=wechatalarm_tmp),]

silencealarmactions = [SilenceAlarmAction()]

# all_wechat_alarm_conf = [WeChatAlarmAction([web_hook for _,web_hook in wechat_web_hooks.items()]),]

ALL_RULES = Rules()
ALL_RULES.register(Rule(factor = algo_factor,action=silencealarmactions,memo="silence"))
ALL_RULES.register(Rule(factor = topic_factor,action=topic_wechat_actions,memo="topic"))
ALL_RULES.register(Rule(factor = defalut_factor,action=ops_wechat_actions,memo="default"))
