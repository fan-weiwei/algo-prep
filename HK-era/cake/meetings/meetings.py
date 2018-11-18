#meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#meetings = [(1, 5), (2, 3)]


## Actually you should sort first!


meetings =  [(1, 10), (2, 6), (3, 5), (7, 9)]
def intersect(range1, range2):
    if range1[0] <= range2[0] and range1[1] >= range2[0]: return True
    if range2[0] <= range1[0] and range2[1] >= range1[0]: return True
    return False




def merge_two(range1, range2):

    if intersect(range1, range2):
        start = min(range1[0], range2[0])
        end = max(range1[0], range2[0])
        return [(min(range1[0],range2[0]),max(range1[1], range2[1]))]
    else:
        return [range1, range2]

#naive:
def merge_ranges(ranges):

    result = [ranges[0]]
    for i in ranges[1:]:
        for j in result:
            if intersect(i,j):
                result.remove(j)
                result += merge_two(i, j)
                break

        else:
            result.append(i)

    return result







print(merge_ranges(meetings))


