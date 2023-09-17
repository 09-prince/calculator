print("WELCOME TO CALCULATOR>>>")
while True:
    print("Please select ::::")
    print('''
    Add --------- 1
    Subtract ---- 2
    Multiply ---- 3
    Divide ------ 4
    ''')

    select=int(input("Please enter 1,2,3,4 ??: "))
    if select in (1,2,3,4):
            try:
                num1=int(input("Enter first number: "))
                num2=int(input("Enter second number: "))
            except ValueError:
                print("Invalid input, Please enter a number :< ")
                continue

            class cal:


                def __init__(self,num,num2) -> None:
                    self.num=num
                    self.num2=num2

                def add(self):
                    print(f'The addition of two number is {self.num+self.num2}')
                def sub(self):
                    print(f"The subtraction of two number is {self.num-self.num2} ")
                def mul(self):
                    print(f"The multiplication of this number is {self.num*self.num2}")
                def div(self):
                    print(f"The division of two number is {self.num/self.num2}")
            total=cal(num1,num2)
            if select==1:
                total.add()
            elif select==2:
                total.sub()
            elif select==3:
                total.mul()
            elif select==4:
                total.div()
            calculate=input("If you want to calculate again :: (yes/no)")
            if calculate!="yes":
                    break
    else:
         print("Invalid output")
print("Thank you :>")
    
