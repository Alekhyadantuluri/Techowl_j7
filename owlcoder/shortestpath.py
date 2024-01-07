m,a,b= map(int,input().split())
n = a^b
c = 0
for i in range(32):
    if n&(1<<i) == (1<<i):
        c+=1
if c%2 !=0:
    print(-1)
else:
    print(c//2)
