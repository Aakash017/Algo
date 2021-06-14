def tappin_rain(_arr):
    _max_storage = 0
    for _index in range(1, len(_arr) - 1):
        _left_max = 0
        #check left max
        for j in range(0, _index):
            _left_max = max(_left_max, _arr[j])
        _right_max = 0
        for k in range(_index+1, len(_arr)):
            _right_max = max(_right_max, _arr[k])
        #print(_index, _arr[_index], _left_max, _right_max)
        _max_storage += min(_left_max, _right_max) - _arr[_index]
    print(_max_storage)


a = [3,0,3,0,1,4]
tappin_rain(a)