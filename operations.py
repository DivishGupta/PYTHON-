a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
n=int(input("how many time you want to perform operation "))
for i in range(0,n):
 c = str(input("enter the operation number "))
 if(c=="1"):
    print(a+b)
 elif(c=="2"):
      print(a-b)
 elif(c=="3"):
    print(a/b)
 elif(c=="4"):
    print(a*b)
 elif(c=="5"):
    print(a%b)
 else:
    print("please inter the valid choice\t")