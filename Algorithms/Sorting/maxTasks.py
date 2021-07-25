def maximum_completed_tasks(n, t, task_difficulties):
    task_difficulties.sort() # 10, 20, 22, 23, 24

    pd = task_difficulties[0] # n is atleast 1
    if pd > t: return 0 # No task could be completed

    timeTaken, nTasks = pd, 1 # 10, 1
    for i in range(1, n):
        cd = task_difficulties[i]
        s = abs(cd-pd)
        ec = cd + s # Execution cost of next task
        if ec + timeTaken <= t:
            timeTaken += ec
            nTasks += 1
            pd = cd

    return nTasks

print(maximum_completed_tasks(5, 65, [24, 23, 22, 10, 20]))
