    def maxSubArraySum(self,arr):
        ##Your code here
        max_sum = arr[0]
        curr_sum = arr[0]
        i = 1
        while i < len(arr):
            if 0 < curr_sum+arr[i]:
                curr_sum += arr[i]
            else:
                curr_sum = arr[i]
            max_sum = max(max_sum, curr_sum)
            
            i+=1
        max_sum = max(max_sum, curr_sum)
        return max_sum
