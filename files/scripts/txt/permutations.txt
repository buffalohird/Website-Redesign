# Calculates the number of permutations of a set
# taking a set and a bool, which determines whether
# or not only unique permutations should be returned
import sys, itertools

def unique(full_set):
    seen = set()
    for x in full_set:
        if x in seen:
            continue
        seen.add(x)
        yield x

def find_all_permutations(list, unique_bool):
    length = len(list) 
    counter = 0
    if unique_bool == True:
      for a in unique(itertools.permutations(list)):
        counter += 1
    else:
      for a in itertools.permutations(list):
        counter += 1
    print counter
        


#Module 14, Sample 4
list1 = ['E','E','E','T','T','S','M']
find_all_permutations(list1 , False)

#Extra
list2 = [1,2,3,4,5,'e','f',6]
final_all_permutations(list2, True)