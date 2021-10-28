def rangeAnd(M, N):
    flipped = 0
    while M != N:
        flipped += 1
        M >>= 1
        N >>= 1
    while flipped:
        M <<= 1
        flipped -= 1
    return M

print(rangeAnd(16, 19))
