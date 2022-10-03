n=int(input())
l_s=input().split()
l_n=[]
for i in l_s:
    l_n.append(int(i))
c=0
for i in range(len(l_n)-1):
    if l_n[i+1]<l_n[i]:
        l_n[i+1]+=1

        c+=1
        
print(c)
