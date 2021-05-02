from .. import Vanilla

from qiime2.plugin import Str, Choices

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
        'case_mod': str % ['all', 'none', 'inverse'],
        },
    outputs={},
    name='sprinkles',
    description=('Changes the case of the text in a Vanilla artifact')
)
