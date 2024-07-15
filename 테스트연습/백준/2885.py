import sys

def main():
    K = int(sys.stdin.read().strip())
    size = 1
    cuts = 0
    pieces = 0

    # Find the smallest 2^n >= K
    while size < K:
        size *= 2
    
    # Calculate minimum cuts needed
    while pieces < K:
        if pieces + size <= K:
            pieces += size
        else:
            size //= 2
            cuts += 1

    print(size, cuts)

if __name__ == "__main__":
    main()
