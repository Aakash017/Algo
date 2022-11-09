"""
100 doors python coding problem



    There are 100 doors in a row that are all initially closed.

    You make 100 passes by the doors.

    The first time through, you visit every door and toggle its state (if the door is closed, you open it; if it is open, you close it).

    The second time, you only visit every 2nd door (door #2, #4, #6, …), and toggle it.

    The third time, you visit every 3rd door (door #3, #6, #9, …).

    Continue this pattern until you only visit the 100th door.

    Which doors are open and which are closed after the last pass?

"""
from math import sqrt

doors = [False] * 101
print(doors)
for i in range(1, 101):
    for j in range(1, 101, i):
        doors[j] = not doors[j]
print(doors)
for d in range(1, 101):
    if doors[d]:
        print(d-1)

for i in range(1, int(sqrt(100))+1):
    print(i*i)
