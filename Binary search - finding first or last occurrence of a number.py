class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
         Since it is asking to write solution in O(log n) time we can use binary search
        '''
        def binarySearch(nums,target,bais):
            l,r = 0, len(nums) - 1
            idx = -1
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    idx = mid
                    if bais:
                        r = mid - 1
                    else:
                        l = mid + 1
            return idx    
                    
        left = binarySearch(nums,target,True)
        right = binarySearch(nums,target,False)
        return [left,right]
        

# leetcode solution /////////
