# Find 3 largest numbers in an array
l = [33,50,34,78,90,23]
t = []
for i in range(3):
    t.append(max(l)) if max(l) not in t else t
    l.remove(max(l))
print(t)
first,second, third=l[0],min,min

for i in range(len(l)):
    if l[i]>firts:
        third=second
        second=first
        first=a[i]



