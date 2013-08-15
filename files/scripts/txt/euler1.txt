def multiples_3_and_5(min, max):
    if max < min:
        false
    sum = 0
    for i in range(min, max):
        if(i % 3 == 0 or i % 5 == 0):
            sum += i
    print sum

multiples_3_and_5(0,1000)
