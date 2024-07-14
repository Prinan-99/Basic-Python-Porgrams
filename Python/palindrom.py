def is_palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    word = "racecar"
    print(f"Is '{word}' a palindrome? {'Yes' if is_palindrome(word) else 'No'}")
