n=int(input())
seq=input()
l_seq=seq.split(sep=" ")
if len(l_seq)<n:
    mx=max(l_seq)
    mn=min(l_seq)
    reqr=list(range(int(mn),int(mx)+1))
    for i in reqr:
        if str(i) not in l_seq:
            print(i)
