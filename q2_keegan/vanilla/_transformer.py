from . import VanillaBeanFmt
from ..plugin_setup import plugin


@plugin.register_transformer
def _vanilla_bean_to_py_list(ff: VanillaBeanFmt) -> list:
    with ff.open() as fh:
        return [i.strip('\n') for i in fh.readlines()]


@plugin.register_transformer
def _py_list_to_vanilla_bean(in_list: list) ->  VanillaBeanFmt:

    ff = VanillaBeanFmt()

    with ff.open() as fh:
        for item in in_list:
            fh.write(str(item.rstrip('\n') + '\n'))

    return ff
