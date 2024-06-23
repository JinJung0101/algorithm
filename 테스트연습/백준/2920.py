musicNote = list(map(int, input().split()))

ascM = sorted(musicNote)
desM = sorted(musicNote, reverse=True)

if musicNote == ascM:
    print("ascending")
elif musicNote == desM:
    print("descending")
else:
    print('mixed')