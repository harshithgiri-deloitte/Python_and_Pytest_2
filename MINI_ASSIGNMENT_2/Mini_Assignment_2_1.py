List1 = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]
for i in List1:
    temp = {}
    for j in i:
        if j in temp:
            temp[j] += 1
        else:
            temp[j]=1
    for i in temp:
        if temp[i] > 1:
            print("{} --> {}".format(i,temp[i]))