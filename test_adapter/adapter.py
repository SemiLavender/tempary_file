from test_adapter.base import MyBase
from test_adapter.base import object_dic


class Adaptor(MyBase):
    def work(self, msg):
        pass

    @classmethod
    def solution(cls, data):
        flag = data['flag']
        msg = data['msg']
        return object_dic[flag](msg)