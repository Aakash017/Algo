def search(arr, k):
    c = 0
    for i in arr:
        c += 1
        print(c)
        if i == k:
            return True
    return False


# print(search([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210,
#               220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420,
#               430, 440,
#               450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650,
#               660, 670,
#               680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880,
#               890, 900,
#               910, 920, 930, 940, 950, 960, 970, 980, 990], 540))

# temp = []
# l1 = [10, 20, 15, 25, 15, 10]
# for i in l1:
#     if i not in temp:
#         temp.append(i)

prime = []
for i in range(1, 101):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
    if is_prime:
        prime.append(i)
# print(prime)

s = "AAAABBBCCDAAAABHHH"

t = []
c=1
for i in range(len(s)-1):
    if s[i] == s[i + 1]:
        c += 1
        if t:
            t.pop()
    else:
        c = 1
    t.append((c, s[i+1]))

# print(t)
s=""
for i in t:
    c,a=i
    s+=str(c)+a

print(s)


# Python3 program to implement
# run length encoding
def printRLE(st):

    t = []
    c=1
    s=""
    for i in range(len(st)-1):
        if st[i] == st[i + 1]:
            c += 1
            if t:
                t.pop()
        else:
            c = 1
        t.append((c, st[i+1]))
    for i in t:
        c,a=i
        s+=str(c)+a
    print(s)

# Driver code
if __name__ == "__main__":

	st = "wwwwaaadexxxxxxywww"
	printRLE(st)