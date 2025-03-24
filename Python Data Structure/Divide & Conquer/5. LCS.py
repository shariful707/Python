def LCS(s1,s2,ind1=0,ind2=0):
    if ind1 == len(s1) or ind2 == len(s2):
        return 0
    elif s1[ind1] == s2[ind2]:
        return 1+ LCS(s1,s2,ind1+1,ind2+1)
    else:
        op1 = LCS(s1,s2,ind1,ind2+1)
        op2 = LCS(s1,s2,ind1+1,ind2)
        return max(op1,op2)

print(LCS('Table','table'))