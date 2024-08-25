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



# 다른 풀이  ---------------------------------------

import sys
input = sys.stdin.read

def classify_triangle(sides):
    a, b, c = sorted(sides)
    if a + b <= c:
        return "Invalid"
    if a == c:
        return "Equilateral"
    elif a == b or b == c:
        return "Isosceles"
    else:
        return "Scalene"

def process_input(data):
    lines = data.strip().split('\n')
    triangles = (map(int, line.split()) for line in lines)
    return [classify_triangle(triangle) for triangle in triangles if not all(x == 0 for x in triangle)]

def main():
    data = input()
    results = process_input(data)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
