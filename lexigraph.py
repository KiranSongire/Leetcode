'''
1. if len(s) ==1 reutrn ""
1. set calculate for n
2. check set length
3. if set length is 1 then
    1. check if first character is a
        1. if a replace b
    2. else replace a
4.  if set is not 1 
    1. for every character check if it is not a 
        1. then replace by a and return the string
    2. if it is a then check next character


Conditions handled:
1. aabccba
2. aaaaa
3. a
    

'''


for i in range(10):
    print(i)



# def breakPalindrome(palindrome):
#     if len(palindrome) == 1:
#         return ""
#     char_set = set(palindrome)
#     if len(char_set) == 1:
#         if palindrome[0] == "a":
#             palindrome = palindrome[:len(palindrome)-1] + "b"
#         else:
#             palindrome = palindrome[:len(palindrome)-1] + "a"
#         return palindrome
#     else:
#         for char in range(len(palindrome)):
#             print(char)
#             if palindrome[char] != "a":
#                 palindrome = palindrome[:char]+ "a" + palindrome[char+1:]
#                 print(palindrome)
#                 return palindrome
            

    

        




# print(breakPalindrome("aa"))