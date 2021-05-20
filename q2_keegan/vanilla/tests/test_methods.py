import os.path
import unittest

from qiime2 import Artifact
from qiime2.plugin.testing import TestPluginBase

class TestMethods(TestPluginBase):
    package = 'q2_keegan.vanilla.tests'


    def _test_data_conversion(case_mod, ascend, descend):

        test_data = ['Sphinx of Black Quartz', '', 'Judge my Vow']

        case_methods = {'invert': str.swapcase,
                        'lower': str.lower,
                        'upper': str.upper,
                        }
        case_method = case_methods[case_mod]

        test_list = []

        for i in test_data:
            test_list.append(case_method(i))

        if ascend:
            test_list.sort()
        if descend:
            test_list.sort(reverse=True)

        return test_list


    def test_sprinkle(self):

        filepath = self.get_data_path(os.path.join('method-txt.qza'))
        test_qza = Artifact.load(filepath=filepath)

        good_cases = {
                'sprinkle_invert': ('invert', False, False),
                'sprinkle_lower': ('lower', False, False),
                'sprinkle_upper': ('upper', False, False),
                'sprinkle_invert_ascending': ('invert', True, False),
                'sprinkle_lower_ascending':('lower', True, False),
                'sprinkle_upper_ascending': ('upper', True, False),
                'sprinkle_invert_descending': ('invert', False, True),
                'sprinkle_lower_descending': ('lower', False, True),
                'sprinkle_upper_descending': ('upper', False, True),
                }
        bad_cases = {
                'sprinkle_both_sort': ('invert', True, True),
                }
        print('\n')

        # Make sure sprinkle produces correct output given good inputs
        for out_name, params in good_cases.items():
            obs, = self.plugin.methods['sprinkle'](
                    test_qza,
                    capitalization=params[0],
                    sort_ascending=params[1],
                    sort_descending=params[2])
            obs = obs.view(list)
            exp = TestMethods._test_data_conversion(params[0],
                                                   params[1],
                                                   params[2])
            self.assertEqual(obs, exp)

        # Test failure given bad input
        for out_name, params in bad_cases.items():
            with self.assertRaisesRegex(ValueError, 'No solution for inputs'):
                obs, = self.plugin.methods['sprinkle'](
                           test_qza,
                           capitalization=params[0],
                           sort_ascending=params[1],
                           sort_descending=params[2])


if __name__ == '__main__':
    unittest.main()
