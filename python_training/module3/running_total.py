
t=int(input())
time=int(input())
s,c=[],[]
st=0
for i in range(t):
    f=int(input())
    c.append(f)
for i in range(t-1):
     st=c[i]+c[i+1]
     count=1
     j=i+2
     while count<time-1 and j<t:
        count=count+1 
        st=st+c[j]
        j=j+1
     s.append(st)   
     
print(max(s))

