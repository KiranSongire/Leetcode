def winnerOfGame(colors):
    A = 0
    B = 0
    for i in range(1, len(colors)-1):
        if colors[i] == "A" and colors[i-1] == "A" and colors[i+1] == "A":
            A = A + 1
        elif colors[i] == "B" and colors[i-1] == "B" and colors[i+1] == "B":
            B = B + 1
    if A > B:
        return True
    else:
        return False
    

print(winnerOfGame("AAABABB"))
