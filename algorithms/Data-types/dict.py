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
