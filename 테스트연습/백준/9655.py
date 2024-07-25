def determine_winner(n):
    if n % 2 == 1:
        return "SK"
    else:
        return "CY"

n = int(input())
print(determine_winner(n))
