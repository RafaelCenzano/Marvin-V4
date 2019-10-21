from . import marvin
from . import physics_helpers

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    # simple test to show that test system works
    def test_absolute_truth_and_meaning(self):
        assert True

    # practice test
    def test_core_func(self):
    	self.assertEqual(marvin.core.func(), "hello")

    def test_sig_fig_counter(self):
    	self.assertEqual(physics_helpers.numberProcessing.count_sig_figs(5), 1)


if __name__ == '__main__':
    unittest.main()