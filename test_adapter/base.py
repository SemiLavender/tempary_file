import abc


class MyBase:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def work(self, msg):
        return


class Student(MyBase):
    flag = 'stu'

    def work(self, msg):
        print('i am a student!')
        yield getPow(msg)


class Driver(MyBase):
    flag = 'dri'

    def work(self, msg):
        print('i am a driver!')
        yield getPow(msg)


class Cook(MyBase):
    flag = 'coo'

    def work(self, msg):
        print('i am a cooker')
        yield getPow(msg)


def getPow(msg):
    return msg * msg


object_dic = {
    'stu': Student().work,
    'coo': Cook().work,
    'dri': Driver().work
}
