import os

import csv

from . import VanillaBeanFmt, IceCream
from qiime2.plugin import Str, Choices, Bool

from ..plugin_setup import plugin

def syrup() -> VanillaBeanFmt:
    
    ff = VanillaBeanFmt()

    with ff.open() as fh:
        pour = csv.writer(fh, delimiter="\t")
        pour.writerow(['Chocolate Fudge',])

    return ff

plugin.methods.register_function(
    function=syrup,
    inputs={},
    parameters={},
    outputs=[('cute_sent', IceCream)],
    name='syrup',
    description='A tiny proof of concept function'
)

def sprinkle(input_ice_cream: VanillaBeanFmt,
             case_mod: str,
             sort_ascending: bool = False,
             sort_descending: bool = False) -> VanillaBeanFmt:

    contents = []

    with open(input_ice_cream, 'r') as fh:
        for line in fh:
            if line.rstrip():
                contents.append(line)

    # Sort if appropriate 
    sort_var = None
    if sort_ascending:
        sort_var=False
    if sort_descending:
        sort_var=True
    if sort_var is not None:
        contents.sort(key=lambda x: x[0].lower(), reverse=sort_var)

    # Apply the desired case transformation
    case_transformer = {
            'all_upper': str.upper,
            'all_lower': str.lower,
            'invert': str.swapcase,
            }[case_mode]

    for i, line in enumerate(contents, 0):
        contents[i] = case_transformer(line)

    return contents

    # sorted_lines = contents.sort()
plugin.methods.register_function(
    function=sprinkle,
    inputs={
        'input_ice_cream': IceCream,
        },
    parameters={
        'case_mod': Str % Choices(['all_upper', 'all_lower', 'invert']),
        'sort_ascending': Bool,
        'sort_descending': Bool,
        },
    outputs={('modified_text', IceCream)},
    name='sprinkles',
    description=('Changes the case of the text in a IceCream artifact.'
                 'Also, you can sort text lines if you want to.')
)
