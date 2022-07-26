*********(https://www.interviewbit.com/problems/square-root-of-integer/hints/) 
Square Root of Integer



class Solution:
  # @param A : integer
  # @return an integer
  def sqrt(self, A):
    left = 0
    right = A
    while left <= right:
      mid = (left + right) // 2
      if mid *mid ==A:
          return mid
          
      elif mid * mid <= A:
        left = mid + 1
      else:
        right = mid - 1
    return right
