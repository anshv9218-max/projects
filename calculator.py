#calculator
class Calculator:
    set_of_instructions=["Type 'start' to use calculator",
                             "Type 'exit' to exit from calculator",
                             "Type operation = sum to find sum of numbers from num1 to num2",
                             "Type operation = factorial to find factorial of both numbers",
                             "Type histroy to acess histroy of past calculations"]
    def __init__(self):
        pass
    #--initiate calculator store value in memory & show histroy--
    def initiate(self):
        for inst in (Calculator.set_of_instructions):
            print(inst)
        while True:
            ins=input("your command: ")
            if ins.lower()=="start":
                print("--PROCEED--\n")
                num1=int(input("first num :"))
                op=input("operator: ")
                num2=int(input("second num ")) 
                self.result=self.calculate(num1,op,num2)
                print(self.result)
                cal.memory(0)
            elif ins.lower()=="histroy":
                cal.memory(1)
                print(self.data)
            elif ins.lower()=="exit":
                print("calculator is terminated sucessfully...")
                break
            else:
                print("--please type correctly 'start' or 'exit'--")
    #--calculate based on operator--
    def calculate(self,num1,op,num2):
        self.num1=num1
        self.op=op
        self.num2=num2
        if self.op=="+":
            return (f"{self.num1+self.num2:.2f}")
        elif self.op=="-":
            return(f"{self.num1-self.num2:.2f}")
        elif self.op=="*":
            return (f"{self.num1*self.num2:.2f}")
        elif self.op=="/":
            return (f"{self.num1/self.num2:.2f}")
        elif self.op=="**":
            return (f"{self.num1**self.num2:.2f}")
        elif self.op in ["sum","natural sum"]:
            sum=0
            for i in range(self.num1,self.num2+1):
                sum=sum+i
            return (f"sum form {self.num1} to {self.num2} is {sum}")
        elif self.op in ["factorial","product","multiply"]:
            self.facto=Calculator.factorial(self)
            return f" factorial of {self.num1} is {self.facto[0]} factorial of {self.num2} is {self.facto[1]}"
        else:
            return ("sorry...not ready for this yet")
        #--factorial method--
    def factorial(self):
        
        fact=1
        for j in range(1,(self.num1+1)):
            fact=fact*j
        f=1
        for j in range(1,(self.num2+1)):
            f=f*j
        fac=[fact,f]
        return fac
    #--memory method to store & read past calculations--
    def memory(self,line):
        self.line=line
        if self.line==0:
            f=open("memory.txt","a")
            f.write(f"\n{self.num1} {self.op} {self.num2} = {self.result}")
            f.close()
        else:
            f=open("memory.txt","r")
            f.seek(0)
            self.data=f.read()
            f.close()
cal=Calculator() # object
cal.initiate()



