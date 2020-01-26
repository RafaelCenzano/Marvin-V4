import decimal

'''
Count significant figures fairly accurately
'''


def count_sig_figs(value):
    '''
    Count the sigfigs of a value
    '''

    if float(value) == 0.0 or abs(float(value)) == 9.8:
        return 90000

    sig_fig_count = 0
    num_list = list(value)

    if num_list[0] == '-':
        remove = num_list.pop(0)

    decimalIndex = -1

    try:
        decimalIndex = num_list.index('.')

    except ValueError:
        pass

    if decimalIndex == -1:

        nonZeroFound = False

        for numbers in num_list[::-1]:

            if numbers != '0':
                nonZeroFound = True
                sig_fig_count += 1

            elif numbers == '0' and nonZeroFound:
                sig_fig_count += 1

    else:

        if float(value).is_integer():

            removed = num_list.pop(decimalIndex)

            s = ''

            return count_sig_figs(s.join(num_list))

        if not zeros:

            nonZeroFound = False

            removed = num_list.pop(decimalIndex)

            for numbers in num_list:

                if numbers != '0':
                    nonZeroFound = True
                    sig_fig_count += 1

                elif numbers == '0' and nonZeroFound:
                    sig_fig_count += 1

    return sig_fig_count


def num_of_zeros(num):
    '''
    Count number of zeros in a string
    '''

    s = '{:.16f}'.format(num).split('.')[1]

    return len(s) - len(s.lstrip('0'))


def properRounding(value, sigFigs):
    '''
    Round values to proper sigfigs including floats or long integers
    '''

    valueSigFigs = count_sig_figs(str(value))

    # when num is int or float that ends in .0
    if isinstance(value, int) or value.is_integer():

        valueCompute = int(value)

        if valueSigFigs > sigFigs:
            newValue = round(valueCompute,
                             sigFigs - (len(str(abs(valueCompute)))))

            return newValue

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

    return typeOfValue == int or typeOfValue == float


def cleanValue(value):
    '''
    Clean up integers that end in .0
    '''

    if value is None:
        return value

    if isinstance(value, float) and value.is_integer():
        return int(value)

    return value


def formCleanup(value):
    '''
    Cleanup inputs from form
    '''

    if value is None:
        return None

    split = [ch for ch in value]

    try:

        if split[len(split) - 2] == '.' and split[len(split) - 1] == '0':
            return float(value)

    except BaseException:
        pass

    check = False

    for items in split:

        if items == '.' and check == False:
            check = True

        elif items == '.' and check:
            return None

    if check:
        return float(value)

    try:

        temp = int(value)
        return temp

    except BaseException:
        return None
