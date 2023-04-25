 
from action import Action
from factor import Factor


class Rule:
    def __init__(self,factor:Factor,action:list,memo:str) -> None:
        self.factor =  factor
        self.action =  action
        self.memo = memo

class Rules:
    rules: list=[]
    def register(self,r:Rule):
        self.rules.append(r)
