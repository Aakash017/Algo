#https://leetcode.com/problems/roman-to-integer/

def romanToInt(self, s: str) -> int:
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    stack = []
    for i in s:
        if not stack:
            stack.append(r[i])
        else:
            if r[i] > stack[-1]:
                new_val = r[i] - stack.pop()
                stack.append(new_val)
            else:
                stack.append(r[i])
    return sum(stack)