from .. import Vanilla

from qiime2.plugin import Str, Choices, Bool

from ..plugin_setup import plugin

def sprinkle(text: Vanilla,
             case_mod: str,
             sort_ascending: bool = False,
             sort_descending: bool = False) -> Vanilla:
    pass

plugin.methods.register_function(
    function=sprinkle,
    inputs={
        'text': Vanilla,
        },
    parameters={
        'case_mod': Str % Choices(['all', 'none', 'inverse']),
        'sort_ascending': Bool,
        'sort_descending': Bool,
        },
    outputs={('modified text', Vanilla)},
    name='sprinkles',
    description=('Changes the case of the text in a Vanilla artifact')
)
