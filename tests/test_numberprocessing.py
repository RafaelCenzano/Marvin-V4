from . import physics_helpers

from nose2.tools import params
import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    @params(20, 700, 0.7, 0.009, 1000, 5)
    def test_sig_fig_counter_for_one(self, value):
        self.assertEqual(physics_helpers.numberProcessing.count_sig_figs(value), 1)

    @params(22, 250, 0.23, 0.0055, 51000)
    def test_sig_fig_counter_for_two(self, value):
        self.assertEqual(physics_helpers.numberProcessing.count_sig_figs(value), 2)

    @params(265, 1250, 0.434, 0.0155, 512, 1.23, 0.701)
    def test_sig_fig_counter_for_three(self, value):
        self.assertEqual(physics_helpers.numberProcessing.count_sig_figs(value), 3)

    @params(1011, 4567, 56.71, 123.7, 1.348, 0.01234, 0.0004444)
    def test_sig_fig_counter_for_four(self, value):
        self.assertEqual(physics_helpers.numberProcessing.count_sig_figs(value), 4)

    @params(9.8, 0)
    def test_sig_fig_counter_for_90000(self, value):
        self.assertEqual(physics_helpers.numberProcessing.count_sig_figs(value), 90000)


if __name__ == '__main__':
    unittest.main()