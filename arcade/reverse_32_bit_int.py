
"""
Assume we are dealing with an environment which could only store integers within the 32-bit signed
integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed
integer overflows.
"""

def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """

    s = str(abs(x))

    reversed = int(s[::-1])

    if reversed > 2147483647:
        return 0

    return reversed if x > 0 else (reversed * -1)