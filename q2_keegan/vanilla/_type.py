from qiime2.plugin import SemanticType

from ..plugin_setup import plugin

from . import VanillaBean, VanillaBeanDirFmt

Vanilla = SemanticType('Vanilla')

plugin.register_semantic_types(Vanilla)


plugin.register_semantic_type_to_format(
    Vanilla,
    artifact_format=VanillaBeanDirFmt
)
