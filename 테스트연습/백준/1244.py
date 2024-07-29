import sys
input = sys.stdin.read

def main():
    data = input().split()
    n = int(data[0])  # 스위치 수
    switches = list(map(int, data[1:n+1]))
    student_count = int(data[n+1])
    students = data[n+2:]

    for i in range(student_count):
        gender = int(students[2*i])
        number = int(students[2*i+1])

        if gender == 1:  # 남학생
            for j in range(number-1, n, number):
                switches[j] = 1 - switches[j]
        elif gender == 2:  # 여학생
            left = right = number - 1
            while left > 0 and right < n - 1 and switches[left-1] == switches[right+1]:
                left -= 1
                right += 1
            for j in range(left, right + 1):
                switches[j] = 1 - switches[j]

    # 출력
    for i in range(0, n, 20):
        print(" ".join(map(str, switches[i:i+20])))

if __name__ == "__main__":
    main()
