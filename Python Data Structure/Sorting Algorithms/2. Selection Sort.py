def SelectionSort(val):
    for i in range(0,len(val)):
        min_ind = i
        for j in range(i,len(val)):
            if val[j] < val[min_ind]:
                min_ind = j
        x = val[i]
        val[i] = val[min_ind]
        val[min_ind] =x


    print(val)
list1 = [9,5,1,3,7,8,4,6]
SelectionSort(list1)