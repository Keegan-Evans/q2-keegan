from . import VanillaBeanFmt
from ..plugin_setup import plugin


@plugin.register_transformer
def _vanilla_bean_to_py_list(ff):
    with ff.open() as fh:
        return [i.strip('\n') for i in fh.readlines()]


@plugin.register_transformer
def _py_list_to_vanilla_bean(in_list):

    ff = VanillaBeanFmt()

    with ff.open() as fh:
        for item in in_list:
            fh.write(str(item.rstrip('\n') + '\n'))

    return ff


# def _one(txt: VanillaBeanFmt) -> list:
#     out_lst = _vanilla_bean_to_py_list(txt)
#     return out_lst
# 
# 
# def _two(lst: list) -> VanillaBeanFmt:
#     return _py_list_to_vanilla_bean(lst)
