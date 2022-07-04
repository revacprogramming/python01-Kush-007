# Functions 


def computepay(h, r):
    if h >40:
        a=h*r
        b=(h-40)*(r*0.5)
        c=a+b
        return c
    else:
        c=h*r
        return c

hrs = float(input("Enter hours: "))
rte = float(input("Enter rate per hour: "))

p = computepay(hrs, rte)
print("Pay", p)