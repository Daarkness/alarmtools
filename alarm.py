from rules import Rules
from action import Action


class AlarmMsg:
    def __init__(self,data:dict,action:Action,other_conf:dict) -> None:
        self.data = data
        self.other_conf = other_conf
        self.action = action

class AlarmManagerAlert:
    def __init__(self,alert_data:dict) -> None:
    
        self._alert_data = alert_data
        self._alert_key = "alerts"
        self._event= {}

    def envet_assort(self,rules:Rules) ->list:

        for alert_s in self._alert_data[self._alert_key]:
            for rule in rules.rules:
                if rule.memo not in self._event:
                    self._event[rule.memo] = {
                        "alert":[],
                        "action":[]
                    }
                        
                
                if rule.factor.check(alert_s):
                    self._event[rule.memo]['alert'].append(alert_s)
                    self._event[rule.memo]['action'] = rule.action
                    break



        # print(self._event)
        alarm_msg_list = []

        for rule_memo , alert_data in self._event.items():
            alarm_msg_list.append(AlarmMsg(
                data=alert_data['alert'],
                action=alert_data['action'],
                other_conf={
                    "memo" : rule_memo,
                }
            ))

        return alarm_msg_list
