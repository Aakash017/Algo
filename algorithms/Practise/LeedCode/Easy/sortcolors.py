def sortColors(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    r, w, b = [], [], []
    for i in nums:
        if i == 0:
            r.append(i)
        elif i == 1:
            w.append(i)
        else:
            b.append(i)
    nums.clear()
    nums.extend(r)
    nums.extend(w)
    nums.extend(b)
    return nums


print(sortColors([1, 2, 2, 2, 0, 1]))
