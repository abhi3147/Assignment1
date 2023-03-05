a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
sign=input("Enter the operation : ")
if sign=='+':
  c=(f"Result is {str(a+b)}")
elif sign=='-':
 c=str(a-b)
elif sign=='*':
  c=str(a*b)
elif sign=='/':
  c=str(a/b)
else:
  print("Operation not possible")
with open("b.txt","w") as file3:
  file3.write(c)
with open("b.txt","r") as file4:
  print(file4.read())
