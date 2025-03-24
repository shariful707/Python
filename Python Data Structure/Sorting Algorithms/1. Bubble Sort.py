def BubbleSort(val):
    for i in range(0,len(val)-1):
        for j in range(0,len(val)-i-1): #len(val)-i == the last elements are sorted then -1 is for in bound range for i =0
            if val[j+1] < val[j]:
                x = val[j+1]
                val[j+1] = val[j]
                val[j] = x

    print(val)

list1 = [9,5,1,3,7,8,4,6]
BubbleSort(list1)