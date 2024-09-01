# 함수 분리: 각 검증 조건을 별도의 함수로 분리하여 코드의 가독성과 재사용성을 높입니다.
# 정규 표현식 사용: 일부 조건을 정규 표현식을 사용하여 간결하게 표현합니다.

import sys
import re

def has_vowel(password):
    return re.search('[aeiou]', password) is not None

def has_three_consecutive_same_type(password):
    return re.search(r'([aeiou]{3,})|([^aeiou]{3,})', password) is not None

def has_double_consecutive(password):
    return re.search(r'([a-z])\1', password) and not re.search(r'(ee|oo)', password)

def is_valid(password):
    if not has_vowel(password):
        return False
    if has_three_consecutive_same_type(password):
        return False
    if has_double_consecutive(password):
        return False
    return True

def main():
    input = sys.stdin.read
    passwords = input().split()
    results = []

    for password in passwords:
        if password == "end":
            break
        valid = is_valid(password)
        message = f"<{password}> is acceptable." if valid else f"<{password}> is not acceptable."
        results.append(message)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
