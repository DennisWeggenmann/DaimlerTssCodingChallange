#test if mergeIntervals works
#Author: Dennis Weggenmann
arr = [[25, 30], [2, 19], [14, 23], [4, 8]]
mergedarr = [[2,23] ,[25,30]]

def test_mergeIntervals():
    from mergeIntervals import mergeOverlappingIntervals
    
    assert mergeOverlappingIntervals(arr) == mergedarr



