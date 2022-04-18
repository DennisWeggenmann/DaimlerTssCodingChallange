def mergeOverlappingIntervals(intervals):
    if len(intervals) == 0:
        return []
    result = []
    # Sort the intervals by start value
    for interval in sorted(intervals, key=lambda x: x[0]):
        #check if there is an overlap and if result is empty
        if result and interval[0] <= result[-1][1]:
            #the ending value is the max of the previous ending value and the current ending value
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            # Add the interval to the result if there is no overlap
            result.append(interval)
    print('merged interval is' , result)
    return result

