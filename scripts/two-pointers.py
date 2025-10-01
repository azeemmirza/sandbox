import time as t

def time_it(func):
  def wrapper(*args, **kwargs):
    start = t.time()
    res = func(*args, **kwargs)
    end = t.time()
    exec_time = end - start
    print(f'execution time: {exec_time:.6f}')
    
    return res
  
  return wrapper


@time_it
def triplet_sum_brute_force(arr: list[int], target = 0) -> list[list[int]]:
  n = len(arr)
  res = []
  
  for i in range(n):
    for j in range(i + 1, n):
      for k in range(j + 1, n):
        
        if arr[i] + arr[j] + arr[k] == target:
          res.append([arr[i], arr[j], arr[k]])
          
          print(f'{arr[i]} {arr[j]} {arr[k]}')
  
  print(res)
  return res



print(triplet_sum_brute_force([0, -1, 2, -3, 1], 0))