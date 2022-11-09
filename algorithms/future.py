nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
target_array = []
# for i in range(len(index)):
#     if target_array[index[i]] is not None:
#         val = target_array.pop()
#         target_array[index[i]] = nums[i]
#     else:
#         target_array[index[i]] = nums[i]
# print(target_array)
for i in range(len(index)):
    target_array.insert(index[i], nums[i])
print(target_array)


def trap(height):
    h = 0
    for i in range(1, len(height) - 1):
        left = height[i]  # Assign current element as left
        for j in range(i):
            left = max(left, height[j])  # Find max of left in array
        right = height[i]  # Assign current elements as right
        for j in range(i + 1, len(height)):
            right = max(right, height[j])  # Find max right in array
        h = h + min(left, right) - height[i]

    print(h)


# trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])


def isValid(s):
    s = list(s)
    l = []
    for i in s:
        if i == "(" or i == "{" or i == "[":
            l.append(i)
        elif i == ")" or i == "}" or i == "]":
            if l:
                if l[-1] == "(" and i == ")":
                    l.pop()
                elif l[-1] == "{" and i == "}":
                    l.pop()
                elif l[-1] == "[" and i == "]":
                    l.pop()
                else:
                    l.append(i)
            else:
                l.append(i)

    if len(l) > 0:
        return False
    else:
        return True


def find_permutations(s):
    s = list(s)
    for i in range(len(s)):
        s[i + 1::] = s[i + 1::-1]
        print(s)


find_permutations("ABC")

s = "ABC"
s = list(s)
print(s[1::])
print(s[1::-1])

# print(s)
