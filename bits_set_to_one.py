def one_bits(x):
    """Given an integer, compute the number of bits set to 1
    Problem from 'Elements of Programming Interviews'.
    """
    m = 1
    count = 0
    for i in range(x // 2 + 1):
        if x & m == m:
            count += 1
        m = m << 1
    return count
