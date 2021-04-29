import re
import qiime2.plugin.model as model
from qiime2.plugin import ValidationError
import qiime2

class vanillaText(model.TextFileFormat):
    
    def validate(self, level):
        """read looks at file to see if there are only ascii [a-z] and [A-Z]
        characters present."""

        disallowedCharacters = {}
        
        with self.open() as fh:
            line = fh.readline()
            for line_number, line in enumerate(fh, start=1):
                lineDisallowedCharacters = []
                raw_line = line.strip().split('\t')
                for char in raw_line:
                    if not re.match(allowedCharacters, char):
                        lineDisallowedCharacters.append(char)
                if lineDisallowedCharacters:
                    disallowedCharacters.
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
                    
