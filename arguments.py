import sys
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
num1=int(sys.argv[1])
operation=sys.argv[2]
num2=int(sys.argv[3])

if operation=='add':
    print(add(num1,num2))
elif operation=='sub':
    print(sub(num1,num2))
elif operation=='mul':
    print(mul(num1,num2))
else:
    print(div(num1,num2))

