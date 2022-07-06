from numpy.core.multiarray import empty
from qiime2.plugin import ValidationError
from pandas import DataFrame
import re
from ._type import IceCream
from ..plugin_setup import plugin

@plugin.register_validator(IceCream)
def validate_characters(data: DataFrame, level):
    accepted_characters = re.compile(r'[a-zA-Z\s]')
    line_char_dict = {}

    for line_number, line in enumerate(data, 1):
        illegal_line_chars = []
        for character in line:
            #if character not in accepted_characters:
            if not re.search(accepted_characters, character):
                illegal_line_chars.append(character)
                print(illegal_line_chars)

        line_char_dict[line_number] = illegal_line_chars

    if line_char_dict:
        raise ValidationError(
                "Contains illegal characters on lines:\n%s" %
                [str(k) + ": " + str(v) for k, v in line_char_dict.items()])
