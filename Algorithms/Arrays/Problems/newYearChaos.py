"""
Constraints:
    - Queue from 1..n
    - Bribe could be given to front person
    - Atmost 2 bribes allowed
    - Move in front
    - If more than two bribes by a person its too chaotic

Goal: Minimum number of bribes

Idea:
- One can move in front from its actual index by giving bribe
- No one else can move you in front by moving backward
- Check diff between actual index and current index
- If diff more than 2 its too chaotic
- For all elements less than the current element, if they are greater they would add to a bribe
  as they have moved in front by giving bribe
"""
def minBribe(q):
    bribes = 0
    for ci, v in enumerate(q):
        ai = v-1 # Actual index
        if ai-ci > 2:
            print("Too chaotic")
            return
        for i in range(ci):
            if q[i] > q[ci]: bribes += 1
    return bribes

def minBribev2(q):
    bribes = 0
    for ci, v in enumerate(q):
        ai = v-1 # Actual index
        if ai-ci > 2:
            print("Too chaotic")
            return
        # We should start checking for greaters after its actual index
        for i in range(max(0, v-2), ci): # 
            if q[i] > q[ci]: bribes += 1
    return bribes

print(minBribe([2, 1, 5, 3, 4]))
print(minBribev2([2, 1, 5, 3, 4]))



