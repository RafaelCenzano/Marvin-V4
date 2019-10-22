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
    def test_proper_rounding_one_integer(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(345, 2), 340)
    def test_proper_rounding_two_integer(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(910.0, 1), 900)
    def test_proper_rounding_three_integer(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(220, 3), 220)
    def test_proper_rounding_four_integer(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(761, 4), 761)
    def test_proper_rounding_five_integer(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(836.0, 5), 836)
    def test_proper_rounding_six_integer(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(562, 1), 600)
    def test_proper_rounding_seven_integer(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(307, 2), 310)
    def test_proper_rounding_eight_integer(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(7683524777, 7), 7683525000)
    def test_proper_rounding_nine_integer(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(-345, 2), -340)
    def test_proper_rounding_ten_integer(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(-35385, 2), -35000)
    def test_proper_rounding_eleven_integer(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(-8783745, 5), -8783700)

    def test_proper_rounding_one_decimal(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(0.345, 2), 0.34)
    def test_proper_rounding_two_decimal(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(0.005, 1), 0.005)
    def test_proper_rounding_three_decimal(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(0.00706, 1), 0.007)
    def test_proper_rounding_four_decimal(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(0.00232, 4), 0.00232)
    def test_proper_rounding_five_decimal(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(0.5006, 3), 0.501)
    def test_proper_rounding_six_decimal(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(0.562, 5), 0.562)
    def test_proper_rounding_seven_decimal(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(0.03, 2), 0.03)
    def test_proper_rounding_eight_decimal(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(0.07683524777, 7), 0.07683525)
    def test_proper_rounding_nine_decimal(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(-0.0345, 2), -0.035)
    def test_proper_rounding_ten_decimal(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(-0.35385, 2), -0.35000)
    def test_proper_rounding_eleven_decimal(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(-0.0008783745, 5), -0.00087837)

    def test_proper_rounding_one_float(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(4.345, 2), 4.3)
    def test_proper_rounding_two_float(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(1.005, 1), 1)
    def test_proper_rounding_three_float(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(55.234, 1), 60)
    def test_proper_rounding_four_float(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(330.222, 3), 330)
    def test_proper_rounding_five_float(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(5.5006, 2), 5.5)
    def test_proper_rounding_six_float(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(7.0095, 4), 7.01)
    def test_proper_rounding_seven_float(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(97.9058, 5), 97.906)
    def test_proper_rounding_eight_float(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(41.097051207, 7), 41.09705)
    def test_proper_rounding_nine_float(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(-2424.0345, 2), -2400)
    def test_proper_rounding_ten_float(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(-72.270512, 6), -72.2705)
    def test_proper_rounding_eleven_float(self):
        self.assertEqual(physics_helpers.numberProcessing.properRounding(-17.6633456781205, 10), -17.66334568)


if __name__ == '__main__':
    unittest.main()