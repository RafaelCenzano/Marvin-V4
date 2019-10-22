'''
Count significant figures fairly accurately
'''


def count_sig_figs(value):
    '''
    This fucntion will count the sigfigs of a value
    '''

    if value == 0 or abs(value) == 9.8:
        return 90000

    sig_fig_count = 0
    num_list = list(str(value))

    for index in range(len(num_list)):

        try:

            fig = int(num_list[index])

            if fig != 0:
                sig_fig_count += 1

            elif checkZeroSig(index, num_list, sig_fig_count):
                sig_fig_count += 1

        except BaseException:
            continue

    return sig_fig_count


def checkZeroSig(index, num_list, sig_fig_count):
    '''
    Checks for significance in a zero from a list
    '''

    try:

        decimal = num_list.index('.')

        if index > decimal and sig_fig_count > 0:
            return True

    except BaseException:

        if index == 0 or index == len(num_list):
            return False

        new_index = index + 1

        if num_list[new_index] == '.' and sig_fig_count > 0:
            return True

        elif num_list[new_index] == '.' and sig_fig_count == 0:
            return False

        elif num_list[new_index] != '.' and sig_fig_count > 0:

            fig = int(num_list[new_index])

            if fig != 0:
                return True

            else:
                return checkZeroSig(new_index, num_list, sig_fig_count)

        elif num_list[new_index] != '.' and sig_fig_count == 0:

            fig = int(num_list[new_index])

            if fig != 0:
                return True

            else:
                return checkZeroSig(new_index, num_list, sig_fig_count)

        else:
            return False


'''
Round Values to sig fig count
'''


def num_of_zeros(num):
    s = '{:.16f}'.format(num).split('.')[1]
    return len(s) - len(s.lstrip('0'))


def properRounding(value, sigFigs):

    valueSigFigs = count_sig_figs(value)

    # when num is int or float that ends in .0
    if isinstance(value, int) or int(value) == value:

        valueCompute = int(value)

        if valueSigFigs > sigFigs:
            newValue = round(valueCompute,
                             sigFigs - (len(str(abs(valueCompute)))))
            return int(newValue)
        else:
            return valueCompute

    # when num is only a decimal
    elif int(value) == 0:

        numOfZeros = num_of_zeros(value)

        if valueSigFigs > sigFigs:
            newValue = round(value, sigFigs + numOfZeros)
            return newValue
        else:
            return value

    # when num is a float
    else:

        if valueSigFigs > sigFigs:

            valueCompute = int(value)

            if len(str(valueCompute)) > sigFigs:
                newValue = round(valueCompute,
                                 sigFigs - (len(str(abs(valueCompute)))))
                return int(newValue)

            elif len(str(valueCompute)) == sigFigs:
                return int(valueCompute)

            else:
                newDecimal = value - int(value)
                newValue = round(newDecimal,
                                 sigFigs - (len(str(abs(valueCompute)))))
                return valueCompute + newValue
        else:
            return value


def checkValue(value):
    '''
    Check value to make sure its an int or float
    '''

    typeOfValue = type(value)

    return typeOfValue == int or typeOfValue == float:
