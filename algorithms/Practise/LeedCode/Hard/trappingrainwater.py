height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def tap_rain_water(height):
    w = 0
    for i in range(len(height)):
        max_left = height[i]
        for j in range(i):
            max_left = max(max_left, height[j])
        max_right = height[i]
        for j in range(i + 1, len(height)):
            max_right = max(max_right, height[j])
        w += min(max_right, max_left) - height[i]
    print(w)




# height = [3, 0, 2, 0, 4]


def optimised_tap_rain_water(height):
    max_left = height[0]
    max_left_arr = []
    for i in range(len(height)):
        max_left = max(max_left, height[i])
        max_left_arr.append(max_left)
    max_right = height[-1]
    max_right_arr = []
    for i in range(len(height) - 1, -1, -1):
        max_right = max(max_right, height[i])
        max_right_arr.append(max_right)
    # print(max_left_arr)
    max_right_arr=max_right_arr[::-1]
    w = 0
    for i in range(len(height)):
        w += min(max_right_arr[i], max_left_arr[i]) - height[i]
    print(w)

tap_rain_water(height)
optimised_tap_rain_water(height)