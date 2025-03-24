def MaximumAmount(List,Index):
    if Index >= len(List):
        return 0
    else:
        FirstHouse = List[Index]+MaximumAmount(List,Index+2)
        NotFirstHouse = MaximumAmount(List,Index+1)
        return max(FirstHouse,NotFirstHouse)

House= [6,7,1,30,8,2,4]
print(MaximumAmount(House,0))