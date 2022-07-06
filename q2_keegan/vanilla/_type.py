from qiime2.plugin import SemanticType

from ..plugin_setup import plugin

from . import VanillaBeanDirFmt

#class HeaderlessType(SemanticType):
#    def __init__(self):
#        self._header = None
#        super().__init__(*args, **kwargs)

IceCream = SemanticType('IceCream')

plugin.register_semantic_types(IceCream)

plugin.register_semantic_type_to_format(
    IceCream,
    artifact_format=VanillaBeanDirFmt
)
