import unittest
import os.path
import csv

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
        filenames = {'obs': 'lst-to-vb.tsv',
                     'exp': 'transformer-test-data.tsv'
                     }

        transformer = self.get_transformer(list, VanillaBeanFmt)
        filepaths = {}
        for each in filenames.keys():
            filepaths[each] = self.get_data_path(filenames[each])
                
        obs = transformer(test_data)

        with obs.open() as obs_file:
            obs = obs_file.readlines()
        with open(filepaths['exp']) as exp_file:
            exp = exp_file.readlines()

        self.assertEqual(obs, exp)
        

if __name__ == '__main__':
    unittest.main()
