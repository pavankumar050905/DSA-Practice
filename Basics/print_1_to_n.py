# Problem: Print 1 to N
# Source: Striver A2Z Sheet

class Solution:
    def printNumbers(self, n):
        if n == 0:
            return
        self.printNumbers(n - 1)
        print(n)
