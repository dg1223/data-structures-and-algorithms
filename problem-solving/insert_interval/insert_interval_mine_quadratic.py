class Solution:
    def overlap(self, next, current):
        return not next[0] > current[1]

    def merge(self, new, old):
        return [min(new[0], old[0]), max(new[1], old[1])]
        
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        # insert at beginning, no overlap
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals

        length = len(intervals)
        # append to end, no overlap
        if newInterval[0] > intervals[-1][1]:
            intervals.insert(length, newInterval)
            return intervals

        # insert in the middle, may have overlap
        for idx, interval in enumerate(intervals):
            # overlap
            if newInterval[0] <= interval[1]:
                merged_interval = self.merge(newInterval, interval)
                intervals[idx] = merged_interval
                break
            # no overlap
            elif idx < length-1 and newInterval[0] > interval[1] and newInterval[1] < intervals[idx+1][0]:
                intervals.insert(idx+1, newInterval)
            else:
                continue

        # calculate length again after initial inserts are done
        length = len(intervals)

        if length > 1:
            counter = length-1
            idx = 0
            while counter > 0:
                current = intervals[idx]
                next = intervals[idx+1] 
                if self.overlap(next, current):
                    merged_interval = self.merge(next, current)
                    intervals[idx] = merged_interval
                    intervals.pop(idx+1)
                    # popping an item will reduce length by 1
                    # since we are overwriting the current idx, we need to stay here
                    # and check for overlap with the next index. So, we decrement 
                    # idx by 1 so that later when we increase it by 1, we still stay
                    # where we currently are
                    idx -= 1
                idx += 1
                counter -= 1

        return intervals