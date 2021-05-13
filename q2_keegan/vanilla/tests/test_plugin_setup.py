import unittest

from q2_keegan.plugin_setup import plugin as keegan_plugin


class PluginSetupTests(unittest.TestCase):

    def test_plugin_setup(self):
        self.assertEqual(keegan_plugin.name, 'keegan')
