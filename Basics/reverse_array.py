# Problem: Reverse an Array using Recursion
# Source: Striver A2Z Sheet

class Solution:
    def reverse(self, arr: list, n: int) -> None:
        
        def helper(left, right):
            if left >= right:
                return
            
            arr[left], arr[right] = arr[right], arr[left]
            helper(left + 1, right - 1)
        
        helper(0, n - 1)
