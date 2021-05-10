import re
import sys

import qiime2.plugin.model as model
from qiime2.plugin import ValidationError

from ..plugin_setup import plugin

class VanillaBeanFmt(model.TextFileFormat):

    def _validate_(self, level):
        accepted_characters = r'[a-zA-Z\s]'
        with self.open() as fh:

            illegal_chars = {}
            
            for line_number, line in enumerate(fh):
                illegal_line_chars = [character for character in line if not 
                    re.match(accepted_characters, character)]
                if illegal_line_chars:
                    illegal_chars[line_number] = illegal_line_chars

            if illegal_chars:
                raise ValidationError(
                        "Contains illegal characters on lines:\n%s" %
                        list(illegal_chars.keys()))


VanillaBeanDirFmt = model.SingleFileDirectoryFormat('VanillaBeanDirFmt',
                                                    'vanillabean.tsv',
                                                    VanillaBeanFmt)
plugin.register_formats(VanillaBeanFmt, VanillaBeanDirFmt)

#plugin.register_views(VanillaBeanFmt, VanillaBeanDirFmt)
