class Calculator:

    def __init__(self,num1,op,num2):
        print("Let's Calculate!")
        self.num1 = num1
        self.num2 = num2
        self.op = op

        self.check_op()


    def check_op(self):
        if self.op == "+":
            self.add()
        elif self.op == "-":
            self.subtract()
        elif self.op == "*":
            self.multiply()
        elif self.op == '/':
            self.divide()

    def add(self):
        val = self.num1+self.num2
        print("The Value of Addition Operation is:",val)

    def subtract(self):
        val = self.num1 - self.num2
        print("The Value of Subtraction Operation is:", val)

    def multiply(self):
        val = self.num1 * self.num2
        print("The Value of Multiplication Operation is:", val)

    def divide(self):
        val = self.num1 / self.num2
        print("The Value of Division Operation is:", val)

cal1 =Calculator(10,'+',2)
cal2 = Calculator(10,'-',2)
cal3 = Calculator(10,'*',2)
cal4 = Calculator(10,'/',2)