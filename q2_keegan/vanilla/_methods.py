import os

import csv

from . import VanillaBeanFmt, IceCream
from qiime2.plugin import Str, Choices, Bool, TypeMap

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

def sprinkle(icecream: VanillaBeanFmt,
             capitalization: str,
             sort_ascending: bool = False,
             sort_descending: bool = False) -> list:

    contents = []

    # Remove Blank Lines
    with icecream.open() as fh:
        for line in fh:
            contents.append(line)

    # Sort if appropriate 
    sort_var = None
    if sort_ascending:
        sort_var = False
    if sort_descending:
        sort_var = True
    if sort_var is not None:
        contents.sort(key=lambda x: x[0].lower(), reverse=sort_var)

    # Apply the desired case transformation
    case_transformer = {
            'upper': str.upper,
            'lower': str.lower,
            'invert': str.swapcase,
            }[capitalization]

    for i, line in enumerate(contents, 0):
        contents[i] = case_transformer(line)

    return contents

sort_ascending, sort_descending, out_text = TypeMap({
    (Bool % Choices([False]),
     Bool % Choices([False])):
     IceCream,
    (Bool % Choices([True]), 
     Bool % Choices([False])):
     IceCream,
    (Bool % Choices([False]), 
     Bool % Choices([True])):
     IceCream,
})

plugin.methods.register_function(
    function=sprinkle,
    inputs={
        'icecream': IceCream,
        },
    parameters={
        'capitalization': Str % Choices(['upper', 'lower', 'invert']),
        'sort_ascending': sort_ascending,
        'sort_descending': sort_descending,
        },
    outputs={('modified', out_text)},
    name='sprinkles',
    description=('Changes the case of the text in a IceCream artifact.'
                 'Also, you can sort text lines if you want to.')
)
