#test if mergeIntervals works
#Author: Dennis Weggenmann
from mergeIntervals import mergeOverlappingIntervals
overlap = [[25, 30], [2, 19], [14, 23], [4, 8]]
overlapResult = [[2,23] ,[25,30]]

noOverlap = [[1,2],[3,4]]
noOverlapResult = [[1,2],[3,4]]
def test_mergeIntervals_noOverlap():
    assert mergeOverlappingIntervals(noOverlap) == noOverlapResult

def test_mergeIntervals():
    assert mergeOverlappingIntervals(overlap) == overlapResult

def test_mergeIntervals_empty():
    assert mergeOverlappingIntervals([]) == []

def test_mergeIntervals_one():
    assert mergeOverlappingIntervals([[1,2]]) == [[1,2]]



