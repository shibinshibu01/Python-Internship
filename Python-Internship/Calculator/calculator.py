class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def subtract(self):
        return self.num1-self.num2
    def divide(self):
        return self.num1/self.num2
    def multiply(self):
        return self.num1*self.num2
    
i=1
while i==1:
    print("======Calculator======")
    
    x=int(input("Enter num1: "))
    y=int(input("Enter num2: "))  
    
    c1=Calculator(x,y) 
    
    j=int(input("1. ADD\n2. SUB\n3. MUL\n4. DIV\n"))
    if j==1:
        result=c1.add()
    elif j==2:
        result=c1.subtract()
    elif j==3:
        result=c1.multiply()
    elif j==4:
        result=c1.divide()
    else:
        print("Invalid")
        result=404
    print("======================")
    print("The result is: ",result)
    print("======================")
    
    i=int(input("Calculate again? (1 to continue)\n"))
        