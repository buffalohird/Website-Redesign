#Finds the expected value and variance
#rolling x number of dies

def calc_die_expected_values(dies):
  expected_value = 0
  expected_values = []
  for x in range(1, 6 * dies + 1):
    expected_values.append(find_die_probability(x, dies))
  counter = 1
  for x in expected_values:
    expected_value += x * counter
    counter += 1
  return expected_value / 6**dies
  
def calc_die_variance(dies):
  expected_value = calc_die_expected_values(dies)
  counter = 0
  values = 0
  for x in range(1, 6 * dies + 1):
    values += (x - expected_value) ** 2
    counter += 1
  return values / counter
     

def find_die_probability(num, dies):
  list = []
  counter = 0
  if dies == 1:
    for i in range(1,7):
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
  
#Module 18, Sample Problem 1
print calc_die_expected_values(1)
print calc_die_variance(1)

print calc_die_expected_values(10)
print calc_die_variance(10)

#Extra Values
print calc_die_expected_values(5)
print calc_die_variance(5)
