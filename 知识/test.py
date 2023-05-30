def cache_decorator(expiration=3 * 60):
    def wrapper(func):
        def news(*args, **kwargs):
            try:
                view = args[0]
                key = view.get_cache_key()
                print(key)
            except:
                key = None
            if not key:
                unique_str = repr((func, args, kwargs))
                print(unique_str)
            value = 1111
            print(value)
            return value

        return news

    return wrapper


@cache_decorator(60 * 60 * 10)  # cache_decorator()return  wrapper
def get_sub_categorys():   # wrapper(get_sub_categorys)
    """
    获得当前分类目录所有子集
    :return:
    """
    categorys = []

    def parse():
        print(111111111111111)
        print(2222)

    parse()
    return categorys

get_sub_categorys() # wrapper(get_sub_categorys())
# cache_decorator(10)(get_sub_categorys)()