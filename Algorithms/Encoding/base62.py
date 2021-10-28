def base62(dec):
    s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    h = ""
    while dec:
        h = s[dec%62] + h
        dec /= 62
    return h
print(base62(999))
        
