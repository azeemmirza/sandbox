def find_divisors(n: int) -> set:
  divisors = set()
  
  for i in range(1, n + 1):
    if n % i == 0:
      divisors.add(i)
  
  
  return divisors

def find_gcd(i: int, j: int) -> dict:
  i_divisors = find_divisors(i)
  j_divisors = find_divisors(j)
  
  common_divisors = set()
  greatest = 0
  
  for i in i_divisors:
    if i in j_divisors:
      common_divisors.add(i)
      if i > greatest:
        greatest = i
  
  return  { 'cd': common_divisors, 'gcd': greatest }


print(find_gcd(12, 30))