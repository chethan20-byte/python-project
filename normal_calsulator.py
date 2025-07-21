def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2


operation={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}

number1=int(input("enter the first number :"))
number2=int(input("enter the second number :"))
for symbol in operation:
    print(symbol)
operation_symbol=input("pic an operation from the line above")    
calculation_function=operation[operation_symbol]
answer=calculation_function(number1,number2)

print(f"{number1} {operation_symbol}{number2}={answer}")