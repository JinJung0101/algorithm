def main():
    import sys
    input = sys.stdin.read
    price = int(input().strip())
    
    change = 1000 - price
    coins = [500, 100, 50, 10, 5, 1]
    
    count = 0
    for coin in coins:
        if change == 0:
            break
        count += change // coin
        change %= coin
    
    print(count)

if __name__ == "__main__":
    main()
