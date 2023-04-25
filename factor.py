
import abc 


class Factor(abc.ABC):
    @abc.abstractmethod
    def check(self,am:dict)->bool:
        pass

class DefalutFactor(Factor):
    def check(self, am: dict) -> bool:   
        return True

caiji_topic_list   = ["t_dc_article_ods", "t_dc_author_ods","t_dc_comment_ods","t_dc_media_ods" ,"t_dc_topic_ods","t_dc_gsdata_xhs_total_ods","t_dc_gsdata_xhs_total_new_ods"]

class TopicFactor(Factor):
    def check(self,alarm_msg:dict)->bool:
        msg_dict  = alarm_msg
        if msg_dict["labels"]["alertname"] == "topic消费延迟" and msg_dict["labels"]["topic"] in caiji_topic_list:
            return  True
        if msg_dict["labels"]["alertname"] == "topic消费异常" and msg_dict["labels"]["topic"] in caiji_topic_list:
            return  True
        return False


class AlgoFactor(Factor):
    def check(self,alarm_msg:dict)->bool:
        msg_dict  = alarm_msg
        if msg_dict["labels"]["alertname"] == "NodeCpuHigh" and "algo" in msg_dict["labels"]["instance"] :
            return  True
        if msg_dict["labels"]["alertname"] == "topic消费延迟" and msg_dict["labels"]["topic"] == "t_dc_author_ods_test":
            return True

        return False


defalut_factor = DefalutFactor()
topic_factor = TopicFactor()
algo_factor = AlgoFactor()
