def missingNumber(self, arr):
    # code here
    arr_sum = sum(arr)
    n = len(arr)
    sum_from_1_to_n = int((n+1)*(n+2)/2)
    return sum_from_1_to_n - arr_sum
