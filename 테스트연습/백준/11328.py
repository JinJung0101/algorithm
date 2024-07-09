import sys
from collections import Counter

input = sys.stdin.read

def main():
    data = input().splitlines()
    n = int(data[0])
    results = []
    
    for i in range(1, n + 1):
        str1, str2 = data[i].split()
        if Counter(str1) == Counter(str2):
            results.append("Possible")
        else:
            results.append("Impossible")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
