import csv

from qiime2.plugin import List
from . import VanillaBeanFmt
from ..plugin_setup import plugin

def _vanilla_bean_to_py_list(ff):
    with ff.open() as fh:
        return [i.rstrip() for i in fh.readlines()]

def _py_list_to_vanilla_bean(in_list):
    
    ff = VanillaBeanFmt()

    with ff.open() as fh:
       # vanillaWriter = csv.writer(fh, delimiter="\t")
        for i in in_list:
            fh.write(str(i + "\n"))

    return ff

@plugin.register_transformer
def _one(txt: VanillaBeanFmt) -> list:
    out_lst = _vanilla_bean_to_py_list(txt)
    return out_lst

@plugin.register_transformer
def _two(lst: list) -> VanillaBeanFmt:
    return _py_list_to_vanilla_bean(lst)
