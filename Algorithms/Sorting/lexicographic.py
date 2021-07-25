"""
def sort_the_files(N, result):
    strings = []
    for i in range(1, N+1):
        strings.append(str(i))
    strings.sort()

    for i in strings[:1000]:
        result.append("IMG{}.jpg".format(i))

def sort_the_files(n, result):
    for i in range(1, n+1):
        result.append("IMG{}.jpg".format(i))
    result.sort()
    del result[1000:]
"""

def sort_the_files(n, result):
    def dfs(num):
        if num > n: return
        if len(result) == 1000: return
        result.append('IMG{}.jpg'.format(num))
        dfs(num*10)
        if num % 10 != 9:
            dfs(num+1)
    dfs(1)

result = []
sort_the_files(16, result)
print(result)
