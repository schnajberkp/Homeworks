def check_palindrome(word):
    # Remove any spaces and convert the word to lowercase
    cleaned_word = word.replace(" ", "").lower()
    # Check if the cleaned word is equal to its reverse
    return cleaned_word == cleaned_word[::-1]

# Example usage:
# print(check_palindrome("racecar"))  # True
# print(check_palindrome("hello"))    # False

print(check_palindrome("racecar"))