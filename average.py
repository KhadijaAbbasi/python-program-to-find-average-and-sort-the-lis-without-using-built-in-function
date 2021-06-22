l=[90,80,90,40,50,60]
sum=0
for i in range(len(l)):
    sum=int(sum)+int(l[i])
avg=int(sum)/len(l)
print(avg)
for x in range(0,len(l)):
    for y in range(0,len(l)):
        if int(l[x])<int(l[y]):
           a=int(l[x])
           l[x]=int(l[y])
           l[y]=int(a)
print(l)