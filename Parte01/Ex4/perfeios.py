#!/usr/bin/env python3

def is_perfect(x):
    sum = 0
    for i in range(1, x):
        if x%i == 0:
            sum += i
    if sum == x:
        return True
    else:
        return False

def print_perfect_numbers(a, b):
    for i in range(a, b+1):
        if is_perfect(i):
            print(i)


print_perfect_numbers(1, 100)


def perfect_Number(n):  #user-defined function
   if n < 1:
      return False

   perfect_sum = 0
   for i in range(1,n):
      if n%i==0:
         perfect_sum += i
   return perfect_sum == n

# take inputs
min_value = 1
max_value = 100

# calling function and print perfect numbers
print('Perfect numbers from %d to %d are:' %(min_value, max_value))
for i in range(min_value, max_value+1):
   if perfect_Number(i):
      print(i, end=', ')