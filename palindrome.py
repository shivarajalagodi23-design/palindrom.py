import sys

def check_palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not a palindrome"

if __name__ == "__main__":
    string = sys.argv[1]

    print("\nPalindrome Check")
    print("----------------")
    print(check_palindrome(string))