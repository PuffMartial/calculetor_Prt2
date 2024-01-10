a = float(input("enter the number A:"))
b = float(input("enter the number B:"))
operator = input("enter the operator:")

if(operator == "+"):
    print(a+b)
elif(operator == "-"):
    print(a-b)
elif(operator == "*"):
    print(a*b)
elif(operator == "/"):
   print(a/b)
else:
  print("invalid operator")