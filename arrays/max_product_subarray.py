def max_product_subarray(arr):
    max_prod = min_prod = result = arr[0]
    
    for num in arr[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        
        result = max(result, max_prod)
    
    return result

def max_product_subarray1(nums):
    if not nums:
        return 0

    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        # If the current number is negative, swap max_product and min_product
        if num < 0:
            max_product, min_product = min_product, max_product

        # Update the max_product and min_product
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)

        # Update the result
        result = max(result, max_product)

    return result

# Example Usage
nums = [2, 3, -2, 4]
print("Maximum product subarray:", max_product_subarray(nums))
