def InsertionSort(val):
    for i in range(0,len(val)-1):
        min = i
        start = i+1
        for j in range(start,0,-1):
            if val[j]<val[j-1]:
                x = val[j]
                val[j]= val[j-1]
                val[j-1] = x
    print(val)

list1 = [9,5,1,3,7,8,4,6]
InsertionSort(list1)