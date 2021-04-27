import re
import qiime2.plugin.model as model
from qiime2.plugin import ValidationError
import qiime2

class vanillaText(model.TextFileFormat):
    
    def validate(self, level):

        """read looks at file to see if there are only ascii [a-z] and [A-Z]
        characters presen"""
        with self.open() as fh:
            line = fh.readline()
            for line_number, line in enumerate(fh, start=0):
                print(line.strip().split('\t'))
