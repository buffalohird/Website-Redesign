#finds the two multiples of pie which share
#the same first two decimal values, guranteed
#by the pigeonhole principle since there are
#101 multiples (including 0) while only 100
#decimal options
from decimal import Decimal

def find_two_same_decimals_of_pie():
  decimals = [0]
  for i in range(1, 101):
    x = 3.14 * i
    x_decimals = number_dec = Decimal(str(x)) % 1
    try:
      x_index = decimals.index(x_decimals)
      return "Multiple Found: Pi is approximately %s / %s" % (i, decimals.index(x_decimals))
    except ValueError:
      decimals.append(x_decimals)
      
      
#Module 1, Small Group 1     
print find_two_same_decimals_of_pie()