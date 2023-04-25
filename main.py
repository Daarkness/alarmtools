from alarm  import AlarmManagerAlert
from register import ALL_RULES
 

 
from flask import Flask,render_template,request
app = Flask(__name__)


import json 

@app.route("/alert/", methods=["post"]) #第二级网页
def alert():
        res = str(request.data, encoding = "utf-8")
        print(res)  
        alarm_msg = json.loads(res)
        alert_s = AlarmManagerAlert(alert_data=alarm_msg)

        alarm_msg_list = alert_s.envet_assort(ALL_RULES)
 

        # __ALL_ALARM_LIST__ = []

        for alarm in alarm_msg_list:
            for i in alarm.action:
                print(alarm.data)
                i.do_aticon(alarm.data)

        return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    print("----")
