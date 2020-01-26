from . import physics, assertEqual, assertTrue, assertFalse


'''
Test Sig Fig Counter for numbers that should return 1, 2, 3, 4, and 9000(special case numbers)
'''


def test_sig_fig_counter_for_one():
    valuesToTest = ['20', '700', '0.7', '0.009', '1000', '5', '-2', '-0.03', '-0.2']
    for value in valuesToTest:
        assertEqual(physics.numberProcessing.count_sig_figs(value), 1)


def test_sig_fig_counter_for_two():
    valuesToTest = ['22', '250','0.23', '0.0055', '51000',
                    '-77', '-0.53', '-0.0034', '92', '0.0055', '4.5', '34','-0.00034', '5.0', '1.0', '51,000']
    for value in valuesToTest:
        assertEqual(physics.numberProcessing.count_sig_figs(value), 2)


def test_sig_fig_counter_for_three():
    valuesToTest = ['265', '1250', '0.434', '0.0155', '512', '1.23', '0.701',
                    '-826', '-93300', '-0.234', '0.903','-0.000999', '50.2', '345', '34.0', '20.1', '4.00', '1.02', '80.0', '231,000']
    for value in valuesToTest:
        assertEqual(physics.numberProcessing.count_sig_figs(value), 3)


def test_sig_fig_counter_for_four():
    valuesToTest = ['1011', '4567', '56.71', '123.7', '1.348', '0.01234', '0.0004444', '-7729',
                    '-2787000', '-0.8633', '-0.2703', '-0.002048', '700.3','200.2', '30.22', '932.0', '204.0', '23.00', '-2.000', '900.0', '923,200', '1,234,000']
    for value in valuesToTest:
        assertEqual(physics.numberProcessing.count_sig_figs(value), 4)


def test_sig_fig_counter_for_90000():
    valuesToTest = ['9.8', '0', '-9.8']
    for value in valuesToTest:
        assertEqual(physics.numberProcessing.count_sig_figs(value), 90000)


'''
Test Zero Counter for number that should return 0, 1, 2, and 3
'''


def test_zero_counter_for_zero():
    valuesToTest = [0.39944, -0.7343, 0.2]
    for value in valuesToTest:
        assertEqual(physics.numberProcessing.num_of_zeros(value), 0)


def test_zero_counter_for_one():
    valuesToTest = [0.0993, -0.09, 0.0349734]
    for value in valuesToTest:
        assertEqual(physics.numberProcessing.num_of_zeros(value), 1)


def test_zero_counter_for_two():
    valuesToTest = [0.005534, -0.007645, 0.003]
    for value in valuesToTest:
        assertEqual(physics.numberProcessing.num_of_zeros(value), 2)


def test_zero_counter_for_three():
    valuesToTest = [0.0003434, -0.000775, 0.000233]
    for value in valuesToTest:
        assertEqual(physics.numberProcessing.num_of_zeros(value), 3)


'''
Test Proper Rounding function
'''


def test_proper_rounding_one_integer():
    assertEqual(
        physics.numberProcessing.properRounding(
            345, 2), 340)


def test_proper_rounding_two_integer():
    assertEqual(
        physics.numberProcessing.properRounding(
            910.0, 1), 900)


def test_proper_rounding_three_integer():
    assertEqual(
        physics.numberProcessing.properRounding(
            220, 3), 220)


def test_proper_rounding_four_integer():
    assertEqual(
        physics.numberProcessing.properRounding(
            761, 4), 761)


def test_proper_rounding_five_integer():
    assertEqual(
        physics.numberProcessing.properRounding(
            836.0, 5), 836)


def test_proper_rounding_six_integer():
    assertEqual(
        physics.numberProcessing.properRounding(
            562, 1), 600)


def test_proper_rounding_seven_integer():
    assertEqual(
        physics.numberProcessing.properRounding(
            307, 2), 310)


def test_proper_rounding_eight_integer():
    assertEqual(
        physics.numberProcessing.properRounding(
            7683524777, 7), 7683525000)


def test_proper_rounding_nine_integer():
    assertEqual(
        physics.numberProcessing.properRounding(-345, 2), -340)


def test_proper_rounding_ten_integer():
    assertEqual(
        physics.numberProcessing.properRounding(-35385, 2), -35000)


def test_proper_rounding_eleven_integer():
    assertEqual(
        physics.numberProcessing.properRounding(-8783745, 5), -8783700)


def test_proper_rounding_one_decimal():
    assertEqual(
        physics.numberProcessing.properRounding(
            0.345, 2), 0.34)


def test_proper_rounding_two_decimal():
    assertEqual(
        physics.numberProcessing.properRounding(
            0.005, 1), 0.005)


def test_proper_rounding_three_decimal():
    assertEqual(
        physics.numberProcessing.properRounding(
            0.00706, 1), 0.007)


def test_proper_rounding_four_decimal():
    assertEqual(
        physics.numberProcessing.properRounding(
            0.00232, 4), 0.00232)


def test_proper_rounding_five_decimal():
    assertEqual(
        physics.numberProcessing.properRounding(
            0.5006, 3), 0.501)


def test_proper_rounding_six_decimal():
    assertEqual(
        physics.numberProcessing.properRounding(
            0.562, 5), 0.562)


def test_proper_rounding_seven_decimal():
    assertEqual(
        physics.numberProcessing.properRounding(
            0.03, 2), 0.03)


def test_proper_rounding_eight_decimal():
    assertEqual(
        physics.numberProcessing.properRounding(
            0.07683524777, 7), 0.07683525)


def test_proper_rounding_nine_decimal():
    assertEqual(
        physics.numberProcessing.properRounding(-0.0345, 2), -0.035)


def test_proper_rounding_ten_decimal():
    assertEqual(
        physics.numberProcessing.properRounding(-0.35385, 2), -0.35000)


def test_proper_rounding_eleven_decimal():
    assertEqual(
        physics.numberProcessing.properRounding(-0.0008783745, 5), -0.00087837)


def test_proper_rounding_one_float():
    assertEqual(
        physics.numberProcessing.properRounding(
            4.345, 2), 4.3)


def test_proper_rounding_two_float():
    assertEqual(
        physics.numberProcessing.properRounding(
            1.005, 1), 1)


def test_proper_rounding_three_float():
    assertEqual(
        physics.numberProcessing.properRounding(
            55.234, 1), 60)


def test_proper_rounding_four_float():
    assertEqual(
        physics.numberProcessing.properRounding(
            330.222, 3), 330)


def test_proper_rounding_five_float():
    assertEqual(
        physics.numberProcessing.properRounding(
            5.5006, 2), 5.5)


def test_proper_rounding_six_float():
    assertEqual(
        physics.numberProcessing.properRounding(
            7.0095, 4), 7.01)


def test_proper_rounding_seven_float():
    assertEqual(
        physics.numberProcessing.properRounding(
            97.9058, 5), 97.906)


def test_proper_rounding_eight_float():
    assertEqual(
        physics.numberProcessing.properRounding(
            41.097051207, 7), 41.09705)


def test_proper_rounding_nine_float():
    assertEqual(
        physics.numberProcessing.properRounding(-2424.0345, 2), -2400)


def test_proper_rounding_ten_float():
    assertEqual(
        physics.numberProcessing.properRounding(-72.270512, 6), -72.2705)


def test_proper_rounding_eleven_float():
    assertEqual(
        physics.numberProcessing.properRounding(-17.6633456781205, 10), -17.66334568)


'''
Test Check Value Function
'''


def test_check_value_int():
    valuesToTest = [23, 24242, 4242, 929329, -2323, -77433, -1, 9]
    for value in valuesToTest:
        assertTrue(physics.numberProcessing.checkValue(value))


def test_check_value_decimal():
    valuesToTest = [0.2324, 0.0025757, 0.000000575,
                    0.5, -0.57, -0.0005757, -0.006]
    for value in valuesToTest:
        assertTrue(physics.numberProcessing.checkValue(value))


def test_check_value_float():
    valuesToTest = [343.23, 340305.34, 5.1,
                    343.0023, -232.34343, -3435.232 - 2.2424]
    for value in valuesToTest:
        assertTrue(physics.numberProcessing.checkValue(value))


def test_check_value_strings():
    valuesToTest = [
        'hello',
        'world',
        'marvin',
        'this is a string',
        'C',
        'B',
        'This should return false']
    for value in valuesToTest:
        assertFalse(physics.numberProcessing.checkValue(value))


def test_check_value_none():
    assertFalse(physics.numberProcessing.checkValue(None))


def test_check_value_lists():
    valuesToTest = [[5, 343], [], [23232, 23, 23, 232],
                    ['hello', 'world'], ['Hello', 'tests']]
    for value in valuesToTest:
        assertFalse(physics.numberProcessing.checkValue(value))


'''
Test cleanup functions
'''


def test_cleanup_num():
    valuesToTest = [5.0, 6.0, 100.0, 30.0, 20, 54, 343.00, -35.0, -466, -250.0]
    for value in valuesToTest:
        assertEqual(physics.numberProcessing.cleanValue(value), int(value))


def test_cleanup_num_none():
    assertEqual(physics.numberProcessing.cleanValue(None), None)


def test_cleanup_form_float_with_zero():
    valuesToTest = [
        '5.0',
        '-6.0',
        '2424.0',
        '239239293.0',
        '238.0',
        '-2323232.0',
        '-7565353.0']
    for value in valuesToTest:
        assertEqual(
            type(
                physics.numberProcessing.formCleanup(value)),
            type(5.1))


def test_cleanup_form_float():
    valuesToTest = [
        '87402.2342343243',
        '32432432.343243243',
        '-34344.434',
        '34343.2',
        '-43534.76655']
    for value in valuesToTest:
        assertEqual(
            type(
                physics.numberProcessing.formCleanup(value)),
            type(5.1))


def test_cleanup_form_integer():
    valuesToTest = [
        '3434',
        '34',
        '99877574890000',
        '304983874839798',
        '-3434',
        '-756646464']
    for value in valuesToTest:
        assertEqual(type(physics.numberProcessing.formCleanup(value)), type(5))


def test_cleanup_form_none():
    valuesToTest = [
        'hello world',
        '5.6.5',
        'ashdjs',
        '984876fasfas',
        '897haoiudh782gbaj',
        '-378tgybuhfjk',
        '353535.353535353.533',
        '-3343.4343.34',
        '-3434.dsfhdf.4343',
        None]
    for value in valuesToTest:
        assertEqual(physics.numberProcessing.formCleanup(value), None)
