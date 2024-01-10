'''l=list(map(int,input().split()))
a = int(input())
for i in range(a):
       m,n=map(int,input().split())
       a=l[m]
       for j in range(m+1,n+1):
           a=a&l[j]
       print(a)
'''
l=list(map(int,input().split()))
m,n=map(int,input().split())
a=[]
res=0
for i in range(len(l)):
       a.append([0]*4)
for j in range(len(l)):
       for k in range(4):
              if l[j]&(1<<k) == 1<<k:
                     a[j][k]=1
for j in range(1,len(l)):
       for k in range(4):
              a[j][k]=a[j-1][k]+a[j][k]

for i in range(4):
       if m==0:
              if a[n][i] == (n-m+1):
                  res+=(1<<i)
       else:
              if a[n][i]-a[m-1][i] == n-m+1:
                  res+=(1<<i)
print(a)
print(res)
           
