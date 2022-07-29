Power Of Two Integers

Q1, Min Steps in Infinite Grid(https://www.interviewbit.com/problems/min-steps-in-infinite-grid/)
  
class Solution:
   
    def coverPoints(self, A, B):
        ans=0
        for i in range(1,len(A)):
            ans=ans+max(abs(A[i]-A[i-1]),abs(B[i]-B[i-1]))
        return ans


Q.2 Max Sum Contiguous Subarray(https://www.interviewbit.com/problems/max-sum-contiguous-subarray/)(kadane's algorithm)

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        length = len(A)
        max_sum = A[0]
        cur_sum = A[0]
        
        for i in range(1,length):
            cur_sum = max(A[i] , cur_sum + A[i])
            max_sum = max(max_sum , cur_sum)
        return max_sum


Q3. Merge Overlapping Intervals(https://www.interviewbit.com/problems/merge-overlapping-intervals/)

class Solution:
    
    def merge(self, intervals):
        intervals.sort(key = lambda interval:interval.start)
        retInterval = []
        first = intervals[0].start
        last = intervals[0].end
        
        for i in range(1, len(intervals)):
            if last > intervals[i].end:
                continue
            elif last < intervals[i].start:
                retInterval.append(Interval(first,last))
                first = intervals[i].start
                last = intervals[i].end
            else:
                last = intervals[i].end
                
        retInterval.append(Interval(first,last))
        return retInterval
                


Q4 Pascal Traingle(https://www.interviewbit.com/problems/pascal-triangle/hints/)

**********
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        l=[[1]]
        if A==0:
            return []
        for i in range(1,A):
            m=[1]
            for j in range(1,i):
                m.append(l[i-1][j-1]+l[i-1][j])
            m.append(1)
            l.append(m)
        return l
***********


def printPascal(n):
    for line in range(1, n + 1):
        C = 1;
        for i in range(1, line + 1):

            print(C, end=" ");
            C = int(C * (line - i) / i);
        print("");
n = int(input());
printPascal(n);
*****


Q.5 Wave Array(https://www.interviewbit.com/problems/wave-array/hints/)

********First approach
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        n = len(A)
        for i in range(0,n-1,2):
            A[i],A[i+1]=A[i+1],A[i]
        return A


********* Second Approach

def sortInWave(arr, n):

    arr.sort()

    for i in range(0, n - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

arr = [10, 90, 49, 2, 1, 5, 23]
sortInWave(arr, len(arr))
for i in range(0, len(arr)):
    print(arr[i], end=" ")



Q6.  Power Of Two Integers(https://www.interviewbit.com/problems/power-of-two-integers/)

******First Approach
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A==1:
            return 1
        
        p=2
        while(2**p<=A):
            pthroot=round(A**(1.0/p),8)
            if int(pthroot)==pthroot:
                return 1
            p+=1
        return 0





