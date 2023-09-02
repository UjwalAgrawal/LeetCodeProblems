def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort(key = lambda x : x[1]) #sort the array by interval's end time
    last_task_end_time = -10000000
    total = 0   #this will give us no of non overlapping intervals (which can be used in other problems)

    #now iterate over the intervals
    for i in intervals:
        if(i[0]>=last_task_end_time):
            total+=1
            last_task_end_time=i[1]
    return(len(intervals) - total)

intervals = [[1,2],[2,3],[3,4],[1,3]] #[start time, end time] fashion
print("Number of intervals needed to make the list non-overlapping is ", eraseOverlapIntervals(intervals))