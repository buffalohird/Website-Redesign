#Finds the number of occurrences the sum appears
#with a supplied number of dice

def find_die_probability(num, dies):
  list = []
  counter = 0
  if dies == 1:
    for i in range(1,6):
      list.append(i)
      if i == num:
        counter += 1
  elif dies == 2:
    for i in range(1,7):
      for j in range(1,7):
        result = i + j
        if result == num:
          counter += 1
  return counter
  
#Module 16, Sample Problem 3
result1 = find_die_probability(7,2) + find_die_probability(11,2)
print "Winning Probability of 7 or 11 for 2 dies is %s of 36" % (result1)
result2 = find_die_probability(2,2) + find_die_probability(3,2) + find_die_probability(12,2)
print "Losing Probability of 2, 3 or 12 for 2 dies is %s of 36" % (result2)
result3win = find_die_probability(4,2)
result3lose = find_die_probability(7,2)
result3total = result3win + result3lose
print "Winning Probability after rolling 4 for 2 dies is %s of %s of (%s of 36)" % (result3win, result3total, result3win)
print "Lose Probability after rolling 4 for 2 dies is %s of  %s of (%s of 36)" % (result3lose, result3total, result3win)

#Extras
for x in range(1, 13):
  print "%s appears %s of 36 times rolling 2 dies" % (x, find_die_probability(x, 2))