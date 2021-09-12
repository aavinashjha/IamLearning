class Stack:
    def __init__(self):
        self.s = list()
    def push(self, x):
        self.s.append(x)
    def top(self):
        # TODO: Empty check
        return self.s[-1]
    def pop(self):
        return self.s.pop()
    def empty(self):
        return len(self.s) == 0

def isBalanced(p):
    s = Stack()
    openCloseMap = {'[': ']', '(': ')'}
    for c in p:
        if c in ('[', '('):
            s.push(c)
        else:
            if s.empty() or c != openCloseMap.get(s.top(), None):
                return False
            s.pop()

    return s.empty()

print(isBalanced("([()])()"))
print(isBalanced("([())()"))
