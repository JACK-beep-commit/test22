# 闭包就是能够读取外部函数内的变量的函数, 获取函数中的变量n
# 闭包是将外层函数内的局部变量和外层函数的外部连接起来的一座桥梁。（下一部分讲解）
# 作用2：将外层函数的变量持久地保存在内存中。
def f1():
    n = 999
    def f2():
        print(n)
    return f2
f = f1()
f()


def tag(tag_name):
    def add_tag(content):
        return "<{0}>{1}</{0}>".format(tag_name, content)

    return add_tag

content = 'Hello'

add_tag = tag('a')
print(add_tag(content))

add_tag = tag('b')
print(add_tag(content))



# 作用2：将外层函数的变量持久地保存在内存中
def create(pos=None):
    if pos is None:
        pos = [0, 0]

    def go(direction, step):
        new_x = pos[0] + direction[0] * step
        new_y = pos[1] + direction[1] * step

        pos[0] = new_x
        pos[1] = new_y

        return pos

    return go


player = create()
print(player([1, 0], 10))
print(player([0, 1], 20))
print(player([-1, 0], 10))


def outer_fun():
    x = 0
    dic = {1:2}
    def inner_fun():
        nonlocal x  # 注意这里,对于不可变数据类型, 如果想改变外部变量,需要加nonlocal
        x = 1
        dic[1] = 3 # 可变数据类型直接引用
        print('inner x:', x, 'at', id(x), "inner dic:", dic, "at", id(dic))

    print('outer x before call inner:', x, 'at', id(x), "inner dic:", dic, "at", id(dic))
    inner_fun()
    print('outer x before call inner:', x, 'at', id(x), "inner dic:", dic, "at", id(dic))


outer_fun()


# 闭包的缺点
# （一）内存消耗
# 由于闭包会使得函数中的变量都被保存在内存中，会增加内存消耗
# 解决
# 在退出函数之前，将不使用的局部变量全部删除。
# （二）使用场景
# 理解清楚这个概念，对于理解 Python 中的一大利器“装饰器”有很大的帮助。因为装饰器本身就是闭包的一个应用
# 如果我们的对象中只有一个方法时，使用闭包是会比用类来实现更优雅, 或者类中的call方法