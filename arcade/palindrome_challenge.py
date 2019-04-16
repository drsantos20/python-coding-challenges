
class Arcade:
    def checkPalindrome(inputString):
        is_palindrome = True
        palindrome_size = len(inputString)-1
        for i in range(len(inputString)):
            if inputString[i] != inputString[palindrome_size-i]:
                is_palindrome = False

        return is_palindrome

    print(checkPalindrome('a'))