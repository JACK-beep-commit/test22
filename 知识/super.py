# super参数解释
# super(), 里面两个参数, 不写或则写当前类默认为父类的方法, 写的父类表示父类的父类方法
# class aa(object):
#     def __init__(self,a=None,b=None):
#         self.a = a
#         self.b = b
#     def bb(self):
#         print("bb")
#     def cc(self):
#         print("cc")
#
# class dd(aa):
#     def __init__(self,a,b,c):
#         super(dd, self).__init__(a,b)
#         # self.a = a
#         # self.b = b
#         self.c = c
#     def ee(self):
#         super(dd, self).cc()
#         print("ee")
#     def ff(self):
#         # self.bb()
#         super().bb()
#
#     def bb(self):
#         print("bbbb")
#         print(self.a)
#         print(self.b)
#         # print(self.e)
#         # print(self.f)
# d =dd("a111","b","c")
# d.ff()
# d.ee()
# # c class, m def. v 常量, f类里面常量
# print(d.__dict__)
# print("*"*10)
# class Parent:
#     def __init__(self, param):
#         self.param = param
#
# class Child(Parent):
#     def __init__(self, param, another_param):
#         super(Child, self).__init__(param)  # 使用父类的参数
#         self.another_param = another_param
#         print(self.param)
#         print(self.another_param)
# Child("aa", "bb")

# class test_class(object):
#     def __init__(self):
#         print(222)
#     def __call__(self, *args, **kwargs):
#         print(1111)
#     def aa(self, *args, **kwargs):
#         print(args.count("a"))
#         print(kwargs.items())
#         print(*args)
#         for i in args:
#             print(i)
#         print(type(args))
#
# t = test_class()
# t.aa("a","b", c="C", e="E")

# import time
# class OnlineMiddleware(object):
#     def __init__(self, get_response=None):
#         print(111)
#         self.get_response = get_response
#         super().__init__()
#
#     def __call__(self, request):
#         ''' page render time '''
#         start_time = time.time()
#         print(start_time)
#         # response = self.get_response(request)
# OnlineMiddleware(11)


#
# class Animal():
#     def __init__(self,name):
#         self.name = name
#
# class Person(Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
#         print('Person')
#
# class Male(Person):
#     def __init__(self,name,age):
#         super(Person,self).__init__(name)
#         print("Male")
#
# m = Male('xiaoming',12)
# super(Male,m).__init__('xiaoming',12)
# print(m.__dict__)
"新增一样"


