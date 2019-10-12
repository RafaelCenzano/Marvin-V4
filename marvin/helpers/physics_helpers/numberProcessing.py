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

            elif check_zero_sig(index, num_list, sig_fig_count):
                sig_fig_count += 1

        except:
            continue

    return sig_fig_count

def check_zero_sig(index, num_list, sig_fig_count):
    '''
    Checks for significance in a zero from a list
    '''

    try:

        decimal = num_list.index('.')

        if index > decimal and sig_fig_count > 0:
            return True

    except:

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
                return check_zero_sig(new_index, num_list, sig_fig_count)

        elif num_list[new_index] != '.' and sig_fig_count == 0:

            fig = int(num_list[new_index])

            if fig != 0:
                return True

            else:
                return check_zero_sig(new_index, num_list, sig_fig_count)

        else:
            return False

def convertToStringFromList(s): 
    '''
    Convert list to string
    '''
    new = ""
   
    for x in s:
        new += x

    return new

def splitString(word): 
    return [char for char in word] 

def properRounding(value, sigFigs):

    splitValue = str(value).split('.')

    splitValueFirst = splitString(str(splitValue[0]))

    print(splitValueFirst)

    count = 0

    for nums in splitValueFirst:

        if nums != 0:
            count += 1

    print(count)

    if count > sigFigs:

        digitsToRemove = count - sigFigs