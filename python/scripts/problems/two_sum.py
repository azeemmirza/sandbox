target = 15
arr = [1, 2, 3, 5, 7, 10, 11, 15]

from typing import List
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' took {end - start:.6f} seconds to run.")
        return result
    return wrapper

@time_it
def solution_01(arr: list, target: int) -> List[int]:
    length = len(arr)
    result = [None] * 2
    
    for i, v1 in enumerate(arr):
      for j, v2 in enumerate(arr[i+1:]):
        print(f'{v1} + {v2} = { v1 + v2 }')
        
        if v1 + v2 == target:
          result = [i, j]
        
    return result


@time_it
def solution_02(arr: list, target: int) -> List[int]:
  left = 0
  right = len(arr) - 1
  
  while left < right:
    sum = arr[left] + right
    
    if sum == target:
      return [arr[left], arr[right]]
    elif sum > target:
      right -= 1
    else:
      left += 1
    
  pass

answer = solution_01(arr, target)
print(answer)

answer_02 = solution_02(arr, target)
print(answer)
  