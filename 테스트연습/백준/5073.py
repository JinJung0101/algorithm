import sys
input = sys.stdin.read

def classify_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

def main():
    data = input().strip().split('\n')
    results = []
    
    for line in data:
        a, b, c = map(int, line.split())
        if a == 0 and b == 0 and c == 0:
            break
        results.append(classify_triangle(a, b, c))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
