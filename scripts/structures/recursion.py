# sum of elements of list using for-loop
def sum_list(nums: list):
  sum = 0
  
  for i in nums:
    sum += i
  
  return sum

# sum of elements of list using recursion (strategy-one)
def sum_list_recursion(nums: list):
  if len(nums) == 1:
    return nums[0]
  
  return nums[0] + sum_list_recursion(nums[1:]) 


# sum using recursion (strategy-two)
def list_sum_recursion_two(
  nums: list,
  low: int = 0,
  high: int | None = None,
  ) -> int:
  if high == None:
    high = len(nums)
  if low >= high:
     pass
  
  return 0


print(sum_list([1, 2, 3, 4, 5, 6]))
print(sum_list_recursion([1, 2, 3, 4, 5, 6]))

# write a function to reverse a list
def reverse_list_recursive(nums: list):
  if len(nums) == 1:
    return [nums[0]]
  
  return [nums[len(nums)-1]]+ reverse_list_recursive(nums[0:len(nums) - 1])


print(reverse_list_recursive([1, 2, 3, 4, 5, 6])) 