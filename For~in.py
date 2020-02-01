def allsum(mylist):
    sum = 0
    for i in mylist:
        sum = sum + i
    return sum


sth_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(allsum(sth_list))

sth_list_2 = range(10)
print(allsum(sth_list_2))
