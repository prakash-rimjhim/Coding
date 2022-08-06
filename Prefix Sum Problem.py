https://leetcode.com/problems/range-sum-query-immutable/
Range Sum Query - Immutable---------- Code


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1] + num)


    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]
        

Q. 2 https://leetcode.com/problems/range-sum-query-mutable/
      Range Sum Query - Mutable----------Code

class NumArray(object):
    def __init__(self, nums):
        self.n = len(nums)
        self.a, self.c = nums, [0] * (self.n + 1)
        for i in range(1, self.n+1):
            self.c[i] += nums[i-1]
            _ = i + (i & -i)
            if _ <= self.n:
                self.c[_] += self.c[i] 

    def update(self, i, val):
        d, self.a[i] = val - self.a[i], val
        i += 1
        while i <= self.n:
            self.c[i] += d
            i += (i & -i)

    def sumRange(self, i, j):
        return self.doSum(j+1, 0) - self.doSum(i, 0)
    
    def doSum(self, i, s):
        while i:
            s += self.c[i]
            i -= (i & -i)
        return s


Q.3 https://leetcode.com/problems/range-sum-query-2d-immutable/
   ***** Range Sum Query 2D - Immutable*****


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for r in range(ROWS+1)]
        
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c+1]
                self.sumMat[r+1][c+1]= prefix + above
        

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, c1, r2, c2 = r1+1, c1+1, r2+1, c2+1
        
        bottomRight = self.sumMat[r2][c2]
        above = self.sumMat[r1 -1][c2]
        left = self.sumMat[r2][c1- 1]
        topLeft = self.sumMat[r1 - 1][c1 - 1]
        
        return bottomRight - above - left + topLeft     

   


