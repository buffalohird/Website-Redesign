return_list = [1]
def find_fibonacci(previous,max, sum):
    if(previous > max):
        return return_list
    if(previous % 2 == 0):
        sum += previous
    new_previous = previous + return_list[-1]
    return_list.append(previous)
    print sum
    find_fibonacci(new_previous, max, sum)
    
find_fibonacci(0, 4000000, 0)
    
