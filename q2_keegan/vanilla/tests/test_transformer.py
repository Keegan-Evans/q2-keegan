import unittest

from q2_keegan.vanilla import VanillaBeanFmt, VanillaBeanDirFmt
from qiime2.plugin.testing import TestPluginBase


class TestTransformers(TestPluginBase):
    package = 'q2_keegan.vanilla.tests'

    def test_vanilla_bean_to_py_list(self):
         filename = 'vb-to-list.tsv'
         test_data = ['foo', 'bar', 'baz']

         filepath = self.get_data_path(filename)

         transformer = self.get_transformer(VanillaBeanFmt, list)

         transformed_data = transformer(filepath)

         self.assertEqual(test_data, transformed_data)

if __name__ == '__main__':
    unittest.main()

