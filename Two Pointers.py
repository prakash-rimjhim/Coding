Q1.  Merge Two Sorted Lists II  (https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/)

******code   First Approach
class Solution:

    def merge(self, A, B):
        A+=B
        A.sort()
        return A
  
****Second Approach

class Solution:

    def merge(self, A, B):
        a=0
        b=0
        while a<len(A) and b<len(B):
            if A[a] > B[b]:
                A.insert(a,B[b])
                b += 1
            else:
                a += 1
        while b<len(B):
            A.append(B[b])
            b += 1
            
        return A  


Q2 . Is Subsequence(https://leetcode.com/problems/is-subsequence/)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        j = 0
        i = 0
        while j < m and i <n:
            if s[j] == t[i]:
                j = j+1
            i = i+1
        return j ==m


Q3 .Two Sum II - Input Array Is Sorted(https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            
            if curSum > target:
                r -= 1
            elif curSum < target:
                l +=1
            else:
                return[l+1 , r+1]
        return []



