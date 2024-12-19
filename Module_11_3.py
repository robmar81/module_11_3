import inspect
from pprint import pprint


def introspection_info(obj):
    att_meth = {'type': type(obj).__name__,
            'attributes': [],
            'methods': []}

    for item in dir(obj):
        if callable(getattr(obj, item)):
            att_meth['methods'].append(item)
        else:
            att_meth['attributes'].append(item)

    obj_module = inspect.getmodule(obj)
    if obj_module is None:
        att_meth['module'] = __name__
    else:
        att_meth['module'] = obj_module.__name__

    return att_meth


if __name__ == '__main__':
    print('-------Проверка для "Интроспекция"')
    pprint(introspection_info("Интроспекция"), compact=True)
    print('-------Проверка для [1, 2, 3, 4, 5, "список"]')
    pprint(introspection_info([1, 2, 3, 4, 5, "список"]), compact=True)

