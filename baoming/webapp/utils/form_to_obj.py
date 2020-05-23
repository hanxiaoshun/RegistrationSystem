
def form_to_obj(form, obj):
    """
    将传入的form 对象的属性值，赋值给对应的model类，使之自动罐装，无需一个一个的拿出来赋值
    :param form:
    :param obj:
    :return:
    """
    obj_dict = obj.__dict__
    print(form)
    print(obj_dict)
    if type(form) is dict:
        # 判断form的类型是否是dict
        if type(obj_dict) is dict:
            for k, v in form.items():
                print(v)
                for key, value in obj_dict.items():
                    # 外键形式会被自动加上_id
                    if key in (k, k+'_id',):
                        k_tmp = k+'_id'
                        print(f'{k},{k_tmp},{key},{v}')
                        obj_dict[key] = v
                    else:
                        pass
        else:
            pass
    else:
        pass

    obj.__dict__ = obj_dict
    return obj


class Black(object):
    """
    测试类
    """

    def __init__(self):
        self.a = ''
        self.b = ''
        self.c = ''
        self.q = ''
        self.o = ''


if __name__ == '__main__':
    form = {'a': 'aaaaa', 'b': 'bbbbbbbb', 'c': 'ccccc'}
    # obj = {'q': '', 'a': '', 'b': '', 'c': '', 'o': ''}
    obj = Black()
    print(obj.__dict__)
    print(form_to_obj(form, obj).__dict__)
