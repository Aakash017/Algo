"""There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it
unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can
 visit all the rooms, or false otherwise."""


# def canVisitAllRooms(rooms):
#     stack = [0]
#     for i in range(0, len(rooms)):
#         for room in rooms[i]:
#             if room != i:
#                 stack.append(room)
#
#     print(stack)
#     # print(list(set(stack)))
#     # print(len(list(set(stack))) == len(rooms))
def canVisitAllRooms(rooms):
    stack = [0]
    visited = set()
    while stack:
        room = stack.pop()
        visited.add(room)
        for key in rooms[room]:
            if key not in visited:
                stack.append(key)
    print (len(visited) == len(rooms))
    # print(d.keys())
    # print(list(set(stack)))
    # print(len(list(set(stack))) == len(rooms))


# print(canVisitAllRooms([[1], [2], [3], []]))
# canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
# canVisitAllRooms([[2], [], [1]])
canVisitAllRooms([[4], [3], [], [2, 5, 7], [1], [], [8, 9], [], [], [6]])
