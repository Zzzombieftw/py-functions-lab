# problem 1
def sum_to(n):
    sum = 0
    for i in range(1, n + 1, 1):
        sum += i
    return sum

print(sum_to(6))  # returns 21
print(sum_to(10)) # returns 55

# problem 2
def largest(list): 
  list.sort()
  return list[-1]

print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))


# problem 3
def occurances(s1, s2):
  return s1.count(s2)


print(occurances('fleep floop', 'e'))
print(occurances('fleep floop', 'p'))
print(occurances('fleep floop', 'ee'))
print(occurances('fleep floop', 'fe'))

def product(*args):
  product = 1
  for n in args:
    product *= n
  return product

print(product(-1, 4)) 
print(product(2, 5, 5)) 
print(product(4, 0.5, 5)) 