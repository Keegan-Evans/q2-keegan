import re
import sys

import qiime2.plugin.model as model
from qiime2.plugin import ValidationError

class Vanilla(model.TextFileFormat):
    def _validate_(self):
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
