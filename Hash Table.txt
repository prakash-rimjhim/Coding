Q 1 --- https://leetcode.com/problems/valid-anagram/submissions/
        VALID ANAGRAM( 2 solutions)
#######
   class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
                                     #########

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a,b=[],[]
        for i in s:
            a.append(i)
        for j in t:
            b.append(j)
        a,b=sorted(a),sorted(b)
        if(len(a)==len(b)):
            for i in range(len(a)):
                if(a[i]!=b[i]):
                    return False
            return True    
        else:
            return False

                      #############################


Q 2   https://leetcode.com/problems/two-sum/
       TWO SUM *********


class Solution(object):
    def twoSum(self, nums, target):
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums [j] == target:
                    ans.append(i)
                    ans.append(j)
        return ans


Q 3 https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
     Count Number of Pairs With Absolute Difference K*********

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        sum = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                
                if  abs(nums [i] - nums[j])==k:
                    sum +=1
                
        return sum
        

Q 4   https://leetcode.com/problems/unique-number-of-occurrences/
              Unique Number of Occurrences******

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a={}
        for i in arr:
            if(i not in a):
                a[i]=0
            a[i]+=1
        return len(a.values())==len(set(a.values()))


