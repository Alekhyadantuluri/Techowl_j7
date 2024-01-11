def seive(n):
    a=[]
    l=[1]*(n+1)
    l[0],l[1]=0,0
    for i in range(2,int(n**0.5)+1):
        if l[i]==1:
            for j in range(i*i,n+1,i):
                l[j]=0
    for i in range(len(l)):
        if l[i]==1:
            a.append(i)
    return a
a = 210
b = 234
c = seive(int(b**0.5))
print(c)
l=[i for i in range(a,b+1)]
for i in range(len(c)):
    if a%c[i]==0:
        for j in range(0,len(l),c[i]):
            l[j]=0
    else:
        res = ((a//c[i])*c[i])+c[i]
        k=res-a
        
        for j in range(k,len(l),c[i]):
            l[j]=0
print(l)
            
