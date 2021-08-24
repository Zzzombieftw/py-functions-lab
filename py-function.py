def sum_to(n):
    sum = 0
    for i in range(1, n + 1, 1):
        sum += i
    return sum



print(sum_to(6))  # returns 21
print(sum_to(10)) # returns 55

