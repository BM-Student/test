def primes_between(x, y):
    temp_list = []
    rang_e = range(x, y+1)
    num_to_y = range(1,y+1)
    for i in rang_e:
        count = 0
        for y in num_to_y:
            if i % y !=0:
                continue
            if i % y == 0 and y != 1 and i != y:
                count += 1
                break
        if count == 0 and i !=1 and i !=-1:
            temp_list.append(i)
    return temp_list

print(primes_between(1, 1000))