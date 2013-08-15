#Finds all numbers between 1 and 10^9 which do not contain
#the japanese unlucky number of 4.  The function is abstracted
#to take any filtering number and a max value for the list

def find_japanese_widgets(excluded, max):
  list = []
  for x in range(1, max):
    list.append(str(x))
  filtered_list = [s for s in list if not str(excluded) in s]
  print filtered_list
  
#Module 14, Sample Problem 3  
find_japanese_widgets(4, 1000000000)

#Extra
find_japanese_widgets(11, 100)
