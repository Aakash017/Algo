d = {11: "Akash", 2: "SASS", 3: "DSESS"}

# Sort a dict based on keys without using sort
s = -9999
t = []
for i in d:
    if i > s:
        t.append(i)

# sort a dict by key
d = {4: 1, 1: 2, 3: 4, 2: 3}
e = sorted(d.items(), key=lambda item: item[1], reverse=True)
print(e)

d = [{"name": "Aakash", "age": 28}, {"name": "Akshat", "age": 24}]
e = sorted(d, key=lambda i: i["age"])
print(e)






































# sort a dict using value

mydict={'a': 100, 'b': 30, 'c': 33, 'd': 14}
# sorted(mydict.items(),key=lambda x:x[1])
# print(mydict)
_sorted_val=sorted(mydict.values())
new_d={}
for v in _sorted_val:
    for key, val in mydict.items():
        if v==val:
            new_d[key]=val
print(new_d)


# sort a dict using key

mydict={'a': 100, 'b': 30, 'c': 33, 'd': 14}

_sorted_key=sorted(mydict.keys())
new_d={}
for k in _sorted_key:
    for key,val in mydict.items():
        if k==key:
            new_d[k]=val
print(new_d)


# using sorted method
mydict={'m': 100, 'b': 30, 'c': 33, 'n': 14}
print(mydict)
sorted(mydict.items(),key=lambda x:x[0])
print(mydict)