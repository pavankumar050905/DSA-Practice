# Problem: Armstrong Number
# Source: Striver A2Z Sheet

class Solution:
    def isArmstrong(self, n):
        tnum = 0
        real = n
        s = n
        suum = 0

        while n > 0:
            tnum += 1
            n //= 10

        while s > 0:
            suum += (s % 10) ** tnum
            s //= 10

        return real == suum
