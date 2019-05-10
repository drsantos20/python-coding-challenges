
class Palindrome:
    def check_palindrome(self, input_string):
        is_palindrome = True
        palindrome_size = len(input_string)-1
        for i in range(len(input_string)):
            if input_string[i] != input_string[palindrome_size-i]:
                is_palindrome = False

        return is_palindrome
