"""You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats
where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time,
provided the sum of the weight of those people is at most limit """


def numRescueBoats(people, limit):
    boats = 0
    people.sort()
    start, end = 0, len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit:
            boats += 1
            start += 1
            end -= 1
        else:
            boats += 1
            end -= 1
    return boats


print(numRescueBoats(people=[3, 5, 3, 4], limit=5))
print(numRescueBoats(people=[1, 2, 3, 4, 5], limit=5))
