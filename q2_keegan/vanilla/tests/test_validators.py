import pandas as pd
from .._validator import validate_characters
from .._format import VanillaBeanFmt
from qiime2.plugin import ValidationError

from qiime2.plugin.testing import TestPluginBase

class TestValidators(TestPluginBase):
    package = 'q2_keegan.vanilla.tests'

    def test_invalid_character_detection(self):
        filename = 'bad_chars.txt'
        filepath = self.get_data_path(filename)

        ff = VanillaBeanFmt(filepath, mode='r')

        with self.assertRaisesRegex(ValidationError, r".*Contains illegal "
                                    "characters on lines.*"):
            validate_characters(ff.view(pd.DataFrame), level='max')
