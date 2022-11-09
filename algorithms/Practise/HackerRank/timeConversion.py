def timeConversion(s):
    # Write your code here
    _time_split = s.split(":")
    _h = _time_split[0]
    if _h == "12" and _time_split[2][2::] == "AM":
        _h = "00"
    elif _h != "12" and _time_split[2][2::] == "PM":
        _h = int(_h)
        _h += 12
    return str(_h) + ":" + _time_split[1] + ":" + _time_split[2][:2]


print(timeConversion("07:05:45PM"))
