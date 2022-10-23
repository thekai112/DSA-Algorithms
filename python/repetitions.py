s=input()
uni_s=[]
for i in s:
    if i not in uni_s:
        uni_s.append(i)
l_c=[]
for i in uni_s:
    l_c.append(list(s).count(i))
print(max(l_c))

     
