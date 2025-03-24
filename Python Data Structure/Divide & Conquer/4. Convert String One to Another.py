def MinOp(s1,s2,ind1,ind2):
    if ind1 == len(s1):
        return len(s2)-ind2
    elif ind2 == len(s2):
        return len(s1)-ind1
    elif s1[ind1]==s2[ind2]:
        return MinOp(s1,s2,ind1+1,ind2+1)
    else:
        delete = 1 + MinOp(s1,s2,ind1,ind2+1)
        insert = 1+ MinOp(s1,s2,ind1+1,ind2)
        replace = 1+ MinOp(s1,s2,ind1+1,ind2+1)
        return min(delete,insert,replace)

print(MinOp('Tbrles','Table',0,0))
