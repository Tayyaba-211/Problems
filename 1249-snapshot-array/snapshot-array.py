import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.data = [{} for _ in range(length)]
        self.history = [ [(0, 0)] for _ in range(length) ]  # Each index keeps list of (snap_id, val)

    def set(self, index: int, val: int) -> None:
        if self.history[index] and self.history[index][-1][0] == self.snap_id:
            self.history[index][-1] = (self.snap_id, val)
        else:
            self.history[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.history[index]
        # Binary search to find the value with snap_id <= target
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1
        return arr[right][1]
