a,b=map(int,input().split())
c=int(input())
for i in range(b,a+1):
    for j in range(i,a+1):
        for k in range(i,j+1):
            if i%k==0 and j%k==0:
                if k==c:
                    print("(",i,",",j,")")
    