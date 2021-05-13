from qiime2.plugin import SemanticType

from ..plugin_setup import plugin

from . import VanillaBeanDirFmt

IceCream = SemanticType('IceCream')

plugin.register_semantic_types(IceCream)

plugin.register_semantic_type_to_format(
    IceCream,
    artifact_format=VanillaBeanDirFmt
)
