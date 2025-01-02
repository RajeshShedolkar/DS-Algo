class Solution:
    def missingNumber(self, arr):
        # code here
        n = len(arr)
        act_sum = ((n+1)*(n+2))//2
        arr_sum = sum(arr)
        return act_sum - arr_sum
