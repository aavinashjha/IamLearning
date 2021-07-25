START = 0
END = 1

class Stack:
    def __init__(self):
        self.s = list()
    def push(self, x):
        self.s.append(x)
    def pop(self):
        return self.s.pop()
    def isEmpty(self):
        return len(self.s) == 0

def cover_the_border(l, radars):
    N = len(radars)
    points = list()
    for i in range(N):
        points.append((radars[i][0], START))
        points.append((radars[i][1], END))

    points = sorted(points, key=lambda x: x[0]) # sort points
    s = Stack()
    border = 0
    for p, boundary in points:
        if boundary == START:
            s.push(p)
        else:
            length = abs(p-s.pop())
            if s.isEmpty():
                border += length
    return border

        
radars = [ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ]
l = 100
print(cover_the_border(l, radars))
