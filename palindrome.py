def palindrome(s):
  s=s.lower().replace(" ","")
  return s==s[::-1]


print(palindrome("A man a plan a canal Panama"))
print(palindrome("Hello"))
