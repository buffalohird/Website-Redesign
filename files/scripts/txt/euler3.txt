"""
The prime factors of 13195 are 5, 7, 13 and 29.
    
What is the largest prime factor of the number 600851475143 ?
    
"""
def find_largest_prime(number):
    largest_prime = 1
    i = 2
    while i < number:
        if number % i == 0:
            if determine_if_prime(i) == True:
                largest_prime = i
                print largest_prime
        i += 1

def determine_if_prime(prime):
    i = 2
    while i < prime:
        if prime % i == 0:
            return False
        i += 1
    return True

find_largest_prime(600851475143)