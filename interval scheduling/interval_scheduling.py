import math

class task():
    def __init__(self, start, finish, weight):
        self.start = start
        self.finish = finish
        self.weight = weight

class schedule():
    def __init__(self, tasks, weight):
        self.tasks = tasks
        self.weight = weight

def interval_scheduling_recursive(t, k, n):
    m = k + 1

    while m < n:
        if (t[k].finish < t[m].finish) & (t[k].finish <= t[m].start):
            return [k] + interval_scheduling_recursive(t, m, n)
        else:
            m += 1

    return [k]


def interval_scheduling_iterative(t, n):
    last_f = 0
    schedule = []

    for m in range(0, n):
        if (last_f < t[m].finish) & (last_f <= t[m].start):
            schedule = schedule + [m]
            last_f = t[m].finish

    return schedule

def task_search(t, n, m, i):
    # find the task 'j' for which t[j].finish is maximum while t[j].finish <= t[i].start
    # find value by running binary search on t[0:i-1]
    # runs in O(log(N))
    l = m - n
    j = n + math.floor(l/2)

    # check for value j
    if (t[j].finish <= t[i].start) & (t[j + 1].finish > t[i].start):
        return j
    elif n == m:
        return -1
    elif t[j].finish <= t[i].start:
        return task_search(t, j, m, i) # search upper half
    else:
        return task_search(t, n, j, i) # search lower half


def linear_task_search(t, i):
    # temp, linear search
    # runs in O(N)
    j = i
    while (j > 0):
        j -= 1
        if t[j].finish <= t[i].start:
            return j
    return -1

def interval_scheduling_weighted(t):
    # runs in O(N log N)
    # assumes tasks are sorted s.t. t[i].finish <= t[i+1].finish holds for 0 <= i < n

    # Rx = { j elem R | s(j) >= x }
    # max 0 <= i < n (w(i) + T(R f(i)))
    # sort by start time?

    n = len(t)
    optimal = schedule([], 0)

    # memoize M[i]
    # for finishing by f[i]
    # optimal sequence
    # weight of optimal sequence
    # this array extends the number of tasks by 1, this allows the index [-1], which maps to [n], to be used for 'NO TASK'
    M = []
    for i in range(0, n + 1):
        M.append(schedule([], 0))

    for i in range(0, n):
        j = task_search(t, 0, i, i)
        choose = t[i].weight + M[j].weight
        leave = M[i - 1].weight
        if choose >= leave:
            M[i] = schedule(M[j].tasks + [i], choose)
        else:
            M[i] = M[i-1]

        if M[i].weight >= optimal.weight:
            optimal = M[i]

    return optimal

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    t = [task(1, 2, 1), task(1, 4, 10), task(3, 4, 1), task(4, 5, 1), task(2, 5, 1), task(7, 9, 1), task(10, 12, 1)]
    n = len(t)

    # test for binary search
    for i in range(1, n):
        j_lin = linear_task_search(t, i)
        j = task_search(t, 0, i, i)
        assert j_lin == j

    schedule_rec = interval_scheduling_recursive(t, 0, n)
    schedule_it = interval_scheduling_iterative(t, n)
    assert schedule_rec == schedule_it

    schedule_weight = interval_scheduling_weighted(t)
    print(schedule_weight.tasks)
