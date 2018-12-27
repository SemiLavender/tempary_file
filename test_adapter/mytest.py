import copy

from test_adapter.adapter import Adaptor

list_test = [
    {'flag': 'stu', 'msg': 2},
    {'flag': 'coo', 'msg': 4},
    {'flag': 'dri', 'msg': 3},
]


def mytest():
    a = ''
    for data in list_test:
        a = Adaptor.solution(data=data)
        print(a)

# mytest()

test_dict = {
    'bytes_ingress': 0,
    'bytes_egress': 1,
    'pkts_ingress': 2,
    'pkts_egress': 3,
    'lbaas_listener_stats': 4,
    'lbaas_member_stats': 5,
}
print(copy.copy('bytes_ingres'))