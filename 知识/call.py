# __call_方法使用,魔法函数,python自行调用
#1. 调用频率较高的函数
#2. 模糊了对象和函数的定义

class AA:
    def __call__(self, *args, **kwargs):
        print("__call__ function exec")
    def test_exec(self):
        print("test_exec is exec")


def execBbj(func):
    return func()




def BB():
    print("bb exec")






# A = AA()
# A() #调用频率较高的函数, 不需要直接A.函数调用
# A.test_exec()
#
# # 模糊了对象和函数的定义,对象和函数都可以直接调用,A表示类实例化之后的对象, BB表示函数
# execBbj(A)
# execBbj(BB)



import time
class OnlineMiddleware(object):
    def __init__(self, get_response=None):
        print(111)
        self.get_response = get_response
        super().__init__()

    def __call__(self):
        ''' page render time '''
        start_time = time.time()
        print(start_time)
        # response = self.get_response(request)
Om = OnlineMiddleware()
Om()






# __getitem__魔法函数使用
# class User:
#     def __init__(self, *args):
#         self.user_list = args[1]
#     def __getitem__(self, item):
#         return self.user_list[item]
#
#     def _test(self):
#         print("test exrc")
#
# user = User(["1","2"],["2","3"])
# for i in user:
#     print("###", i)
# user._test()





