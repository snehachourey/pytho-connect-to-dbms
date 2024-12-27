def sum(a,b):
    return(a+b)
def multi(a,b):
    return(a*b)
res=0
ans='y'
while(ans=='y'):
    num1=int(input("enter an number "))
    num2=int(input("enter an number "))
    print('1.Add')
    print('2.Multiplay')
    choice=int(input("enter an number"))
    if(choice==1):
        res=sum(num1,num2)
        print("result is:",res)
    elif(choice==2):
        res=multi(num1,num2)
        print("result is:",res)
    else:
        print("Invailid choice")
    ans=input("More operation??y/n")
