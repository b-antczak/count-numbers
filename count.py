# Assumes no numbers are joined with "and"
# Assumes no breathing breaks, bathroom breaks, etc.

# NOTE: these are "guesstimates" determined solely on me saying the number
#       out loud and predicting the time it takes to say it
VERBAL_WORD_LENGTH = {
    1: 0.4,
    2: 0.4,
    3: 0.4,
    4: 0.4,
    5: 0.4,
    6: 0.4,
    7: 0.6,
    8: 0.4,
    9: 0.4,
    10: 0.4,
    11: 1.0,
    12: 0.6,
    13: 0.75,
    14: 0.75,
    15: 0.75,
    16: 0.75,
    17: 0.75,
    18: 0.75,
    19: 0.75,
    20: 0.75,
    30: 0.75,
    40: 0.75,
    50: 0.75,
    60: 0.75,
    70: 1.0,
    80: 0.75,
    90: 0.75,
    100: 1.0,
    200: 1.0,
    300: 1.0,
    400: 1.0,
    500: 1.0,
    600: 1.0,
    700: 1.0,
    800: 1.0,
    900: 1.0
}

BATCHES = {
    1: {
        'name': 'thousand',
        'time': 1.1
    },
    2: {
        'name': 'million',
        'time': 1.3
    },
    3: {
        'name': 'billion',
        'time': 1.3
    },
    4: {
        'name': 'trillion',
        'time': 1.4
    }
}

def get_nth_triple(number, n):
    """
    Returns the n-th triple of a number, starting with the 0th triple which contains
    the least significant digits. Returns -1 if invalid index.
    Refer to test-count-numbers.py for examples.
    """
    ret = -1
    pos = 0
    num = number
    factor = 1
    while num >= 1:
        if pos >= n * 3 and pos < (n * 3) + 3:
            if ret < 0:
                ret = 0
            ret += int(num % 10) * factor
            factor *= 10
        elif pos >= (n * 3) + 3:
            break
        num /= 10
        pos += 1
    return ret

def say_number(num):
    """
    Returns the amount of time required to say the given number, in seconds.
    Refer to test-count-numbers.py for examples.
    """
    if num % 1000 != num:
        # Invalid number
        return -1
    n = num
    pos = 0
    total_time = 0
    v = 0
    factor = 1
    first = 0
    while n >= 1:
        r = int(n % 10)
        if pos == 0:
            first = r
        v = r * factor
        if r == 1 and pos == 1:
            # The edge case where our number ends in any number from [11 - 19]
            total_time = VERBAL_WORD_LENGTH[v + first]
        elif v != 0:
            total_time += VERBAL_WORD_LENGTH[v]
        n /= 10
        factor *= 10
        pos += 1
    return total_time

def get_triples(num):
    """
    Returns an array of three-digit numbers that represent the given number in reverse.
    The last element will have at most 3 digits.
    Refer to test-count-numbers.py for examples.
    """
    n = num
    c = 0
    arr = []
    while n % 1000 != n:
        arr.append(get_nth_triple(num, c))
        n = int(n/1000) # shave off those digits
        c += 1
    arr.append(n)
    return arr

def time_to_count_to_num(num):
    """
    Determines the total time required to count from 1 up to the given number.
    """
    print('Loading ...')
    total_time = 0
    for n in range(1, num + 1):
        for index, number in enumerate(get_triples(n)):
            t = say_number(number)
            if index > 0:
                # We also need to consider the time it takes to say 'thousand' or 'million'
                t += BATCHES[index]['time']
            total_time += t
    return total_time

# NOTE: current max is 999,999,999,999,999
print(round(time_to_count_to_num(10000000), 2))
