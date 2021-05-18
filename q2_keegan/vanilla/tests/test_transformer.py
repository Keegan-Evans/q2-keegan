import unittest

from q2_keegan.vanilla import VanillaBeanFmt, VanillaBeanDirFmt
from qiime2.plugin.testing import TestPluginBase


class TestTransformers(TestPluginBase):
    package = 'q2_keegan.vanilla.tests'

    def test_vanilla_bean_to_py_list(self):

        filename = './transformer-test-data.tsv'
        _, obs = self.transform_format(VanillaBeanFmt, list, filename)

        exp = ['foo', 'bar', 'baz']

        self.assertEqual(exp, obs)


    def test_py_list_to_vanilla_bean(self):
        test_data = ['foo', 'bar', 'baz']

        transformer = self.get_transformer(list, VanillaBeanFmt)

        obs = transformer(test_data)
        obs = obs.view(list)
        exp =  test_data
        
        self.assertEqual(obs, exp)
        

if __name__ == '__main__':
    unittest.main()
