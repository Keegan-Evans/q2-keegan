import os
import os.path
import unittest

from q2_keegan.vanilla import VanillaBeanFmt, VanillaBeanDirFmt
from qiime2.plugin.testing import TestPluginBase
from qiime2.plugin import ValidationError

class TestVanillaFormats(TestPluginBase):
    package = 'q2_keegan.vanilla.tests'

    def test_vanilla_format_validate_positive(self):
        filenames = ['single-row-valid.txt', 'multi-row-valid.txt',
                     'multi-row-w-blank-lines-valid.txt',
                     ]
        filepaths = [self.get_data_path(os.path.join('data', filename))
                        for filename in filenames]

        for filpath in filepaths:
            format = VanillaBeanFmt(filpath, mode='r')

            format.validate()

    def test_vanilla_format_validate_negative(self):
        filenames = ['single-row-numbers-non-valid.txt',
                     'single-row-punc-non-valid.txt',
                     'multi-row-numbers-non-valid.txt',
                     'multi-row-punc-non-valid.txt',
                     ]

        filepaths = [self.get_data_path(os.path.join('data', filename))
                        for filename in filenames]

        for filepath in filepaths:
            format = VanillaBeanFmt(filepath, mode='r')
            with self.assertRaisesRegex(ValidationError, 'VanillaBeanFmt'):
                format.validate()
