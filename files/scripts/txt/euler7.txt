"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

def find_specific_prime(specific_prime):
    prime_count = 0
    i = 2
    while prime_count < specific_prime:
        if determine_if_prime(i) == True:
            prime_count += 1
            if prime_count == specific_prime:
                return i
        i += 1
            
def determine_if_prime(prime):
    i = 2
    while i < prime:
        if prime % i == 0:
            return False
        i += 1
    return True
    
print find_specific_prime(10001)