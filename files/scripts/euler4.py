"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def find_largest_palindrome(digits):
    largest_palindrome = 1
    max = 0
    for i in range(0, digits):
        max += 9 * 10 ** i
    print max
    for i in range(0, max):
        for j in range(0, max):
            number = (i * j)
            number_string = str(number)
            if (number_string == number_string[::-1] and number > largest_palindrome):
                largest_palindrome = number
                print largest_palindrome

find_largest_palindrome(3)