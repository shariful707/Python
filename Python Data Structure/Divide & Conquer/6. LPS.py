def LPS(s1,start,end):
    if start>end:
        return 0
    elif start == end:
        return 1
    elif s1[start]==s1[end]:
        return 2+ LPS(s1,start+1,end-1)
    else:
        op2 = LPS(s1, start, end-1)
        op1 = LPS(s1,start+1,end)

    return max(op1,op2)

print(LPS('ELRMENMET',0,len('ELRMENMET')-1))