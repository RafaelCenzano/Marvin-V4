from . import physics_helpers

from nose2.tools import params
import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    @params(22, 250, 0.23, 0.0055, 51000)
    def test_sig_fig_counter(self, value):
        self.assertEqual(physics_helpers.numberProcessing.count_sig_figs(value), 2)


if __name__ == '__main__':
    unittest.main()