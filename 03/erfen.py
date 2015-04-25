def erfen(list,value):
    begin = 0
    if list[0] == value:
        return 0
    end = len(list)-1
    while(begin<end):
        mid = begin + (end-begin)//2
        if list[mid]>value:
            end = mid-1
        elif list[mid]<value:
            begin = mid+1
        else:
            return mid
    if(begin == end):
        if(value == list[begin]):
            return begin
        else:
            return -1
