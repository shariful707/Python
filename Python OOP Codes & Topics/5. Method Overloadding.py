from idlelib.debugobj import dispatch


class Calculator:
    def __init__(self):
        pass

    # @dispatch(int,int)
    # def production(self,a,b):
    #     print(a*b)
    #
    # @dispatch(int,int,int)
    # def production(self,a,b,c):
    #     print(a*b*c)

    def Multiplier(self,*nums):
        sum = 1
        for i in nums:
            sum = sum*i
        print("Total Sum:",sum)

cal = Calculator()
cal.Multiplier(1,2,3,4,5,6)

# cal.production(4,5)
# cal.production(4,5,6)