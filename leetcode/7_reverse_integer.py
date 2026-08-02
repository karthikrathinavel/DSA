class Solution:
    def reverse(self, x: int) -> int: #1534236469
        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        rev = 0
        while x > 0:
            rem = x % 10
            rev = (rev * 10) + rem
            x = x // 10
        if neg:
            rev = -rev
        if rev > (2 ** 31) or rev < -(2 ** 31):
            rev = 0
        return rev
        