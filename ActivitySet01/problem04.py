# Conditional Execution
hrs = input("Enter hours")
rate= input("enter rate")
h=float(hrs)
r=float(rate)
if  h >40:
    a=h*r
    b=(h-40)*(r*0.5)
    pay= a+b
    print(pay)
else:
    pay= hrs*rate
    print(pay)

