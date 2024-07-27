import sys
input = sys.stdin.read

def is_valid(password):
    vowels = "aeiou"
    has_vowel = False
    consecutive_consonant = 0
    consecutive_vowel = 0
    last_char = ""

    for i, char in enumerate(password):
        if char in vowels:
            has_vowel = True
            consecutive_vowel += 1
            consecutive_consonant = 0
        else:
            consecutive_consonant += 1
            consecutive_vowel = 0

        if consecutive_vowel > 2 or consecutive_consonant > 2:
            return False

        if i > 0 and char == last_char and char not in "eo":
            return False

        last_char = char

    return has_vowel

def main():
    data = input().split()
    results = []

    for password in data:
        if password == "end":
            break
        valid = is_valid(password)
        result = f"<{password}> is acceptable." if valid else f"<{password}> is not acceptable."
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
