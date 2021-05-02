from . import VanillaBean
from ..plugin_setup import plugin

def _vanilla_bean_to_py_list(table: VanillaBean) -> list:
    return [i.rstrip() for i in table.split(" ")]
