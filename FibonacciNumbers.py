n=int(input("Enter the number of terms needed : "))
a=0
b=1
print(a,b,end=" ")
for i in range(0,n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")