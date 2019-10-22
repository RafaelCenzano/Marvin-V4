from . import physics_helpers

from nose2.tools import params
import unittest

class BasicTestSuite(unittest.TestCase):

    '''
    Test Sig Fig Counter for numbers that should return 1, 2, 3, 4, and 9000(special case numbers)
    '''
    @params(20, 700, 0.7, 0.009, 1000, 5, -2, -0.03, -0.2)
    def test_sig_fig_counter_for_one(self, value):
        self.assertEqual(physics_helpers.numberProcessing.count_sig_figs(value), 1)

    @params(22, 250, 0.23, 0.0055, 51000, -77, -0.53, -0.0034)
    def test_sig_fig_counter_for_two(self, value):
        self.assertEqual(physics_helpers.numberProcessing.count_sig_figs(value), 2)

    @params(265, 1250, 0.434, 0.0155, 512, 1.23, 0.701, -826, -93300, -0.234, 0.903, -0.000999)
    def test_sig_fig_counter_for_three(self, value):
        self.assertEqual(physics_helpers.numberProcessing.count_sig_figs(value), 3)
	
    @params(1011, 4567, 56.71, 123.7, 1.348, 0.01234, 0.0004444, -7729, -2787000, -0.8633, -0.2703, -0.002048)
    def test_sig_fig_counter_for_four(self, value):
        self.assertEqual(physics_helpers.numberProcessing.count_sig_figs(value), 4)

    @params(9.8, 0, -9.8)
    def test_sig_fig_counter_for_90000(self, value):
        self.assertEqual(physics_helpers.numberProcessing.count_sig_figs(value), 90000)

    '''
    Test Zero Counter for number that should return 0, 1, 2, and 3
    '''
    @params(0.39944, -0.7343, 0.2)
    def test_zero_counter_for_zero(self, value):
        self.assertEqual(physics_helpers.numberProcessing.num_of_zeros(value), 0)

    @params(0.0993, -0.09, 0.0349734)
    def test_zero_counter_for_one(self, value):
        self.assertEqual(physics_helpers.numberProcessing.num_of_zeros(value), 1)

    @params(0.005534, -0.007645, 0.003)
    def test_zero_counter_for_two(self, value):
        self.assertEqual(physics_helpers.numberProcessing.num_of_zeros(value), 2)

    @params(0.0003434, -0.000775, 0.000233)
    def test_zero_counter_for_three(self, value):
        self.assertEqual(physics_helpers.numberProcessing.num_of_zeros(value), 3)

    '''
    Test Proper Rounding function
    '''
    def test_proper_rounding_one(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(345, 2), 340)
    def test_proper_rounding_two(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(910, 1), 900)
    def test_proper_rounding_three(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(220, 3), 220)
    def test_proper_rounding_four(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(761, 4), 761)
    def test_proper_rounding_five(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(836, 5), 836)
    def test_proper_rounding_six(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(562, 1), 600)
    def test_proper_rounding_seven(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(300, 1), 300)
    def test_proper_rounding_eight(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(7683524777, 7), 7683525000)
    def test_proper_rounding_nine(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(-345, 2), -340)
    def test_proper_rounding_ten(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(-35385, 2), -35000)


if __name__ == '__main__':
    unittest.main()