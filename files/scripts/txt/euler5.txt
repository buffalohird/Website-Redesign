"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
def find_smallest_multiple(min, max):
    smallest_multiple = 0
    number = 2
    while(smallest_multiple == 0):
        print number
        if check_smallest_multiple(number, min, max):
            smallest_multiple = number
            return smallest_multiple
        number += 1
            
def check_smallest_multiple(number, min, max):
    for i in range (min, max):
        if number % i != 0:
            return False
    return True
    
print find_smallest_multiple(1,20)