def Letter_Frequency(str1):
    d=dict()
    l=len(str1)
    for key in str1:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    decreasingOrderFrequency = dict(sorted(d.items(), key=lambda x: x[1] , reverse=True))
    for x, y in decreasingOrderFrequency.items():
        print(x,"=", y,end=" ")
s=input("Enter a string : ")
Letter_Frequency(s)

