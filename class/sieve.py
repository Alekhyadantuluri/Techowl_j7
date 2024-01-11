def seive(n):
    l=[1 for i in range(n+1)]
    l[0],l[1]=0,0
    for i in range(2,int(n**0.5)+1):
        if l[i]==1:
            for j in range(i*i,n+1,i):
                l[j]=0
    return l
for i in range(int(input())):
    n = int(input())
    a = seive(n)
    l=[]
    for i in range(len(a)):
        if a[i] == 1:
            l.append(i)
    c = 0
    print(l)
    for j in range(len(l)-1):
        if l[j+1]-l[j] == 2:
            c+=1
print(c)
            
