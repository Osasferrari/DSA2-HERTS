
def isPalindrome(word):
    # Base case: if the length of the word is 0 or 1, it's a palindrome
    if len(word) <= 1:
        return True
    # Recursive case: check if the first and last characters are the same
    if word[0] == word[-1]:
        # Recursively check the substring that excludes the first and last characters
        return isPalindrome(word[1:-1])
    # If the first and last characters are not the same, it's not a palindrome
    return False

# recommended examples
print(isPalindrome("gag"))      # True
print(isPalindrome("pop"))      # True
print(isPalindrome("hannah"))   # True
print(isPalindrome("rotator"))  # True
print(isPalindrome("python"))   # False
