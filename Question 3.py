Check if a string is palindrome or not.
	"abba" => true
	"cd"   => false

***CODE***

def isPalindrome(s):
	return s == s[::-1]

s = input()
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
