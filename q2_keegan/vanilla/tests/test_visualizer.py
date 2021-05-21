import unittest
import os.path
import tempfile

from qiime2 import Artifact
from qiime2.plugin.testing import TestPluginBase
from q2_keegan.vanilla import scooper

import shutil
class TestScooper(TestPluginBase):
    package = 'q2_keegan.vanilla.tests'

    def test_scooper(self):
        filepath = self.get_data_path(os.path.join('method-txt.qza'))
        test_qza = Artifact.load(filepath=filepath)
        test_qza = test_qza.view(list)
        exp = ['<pre>\n', 'Sphinx of Black Quartz\n', '\n', 'Judge my Vow\n',
               '</pre>\n']

        with tempfile.TemporaryDirectory () as output_dir:
            scooper(output_dir,
                    test_qza)

            index_fp = os.path.join(output_dir, 'index.html')

            with open(index_fp, 'r') as ih:
                output_txt = ih.readlines()
                obs = output_txt[32:37]

            self.assertEqual(exp, obs)

if __name__ == '__main__':
    unittest.main()
