def interval_scheduling_recursive(s, f, k, n):

    m = k + 1

    while m < n:
        if (f[k] < f[m]) & (f[k] <= s[m]):
            return [k] + interval_scheduling_recursive(s, f, m, n)
        else:
            m += 1
    
    return [k]



def interval_scheduling_iterative(s, f, n):
    last_f = 0
    schedule = []

    for m in range(0, n):
        if (last_f < f[m]) & (last_f <= s[m]):
            schedule = schedule + [m]
            last_f = f[m]

    return schedule

def interval_scheduling_weighted(s, f, w, n):
        # sort by start time O(n log n)
        
        # Rx = { j elem R | s(j) >= x }
        # max 0 <= i < n (w(i) + T(R f(i)))
        # sort by start time?
    
    W = {} #
    A = {} #
    a = 0
    max = 0

    for i in range(0, n):
        W[s[i]] = 0
        A[s[i]] = []
        W[f[i]] = 0
        A[f[i]] = []

    
    for i in range(0, n):
        # max w(i) + R(f(i)), R(f(i-1))
        take = w[i] + W[s[i]]
        leave = W[f[i - 1]]
        if (take > leave):
            W[f[i]] = take
            A[f[i]] = [i] + A[s[i]]
        else:
            W[f[i]] = leave
            A[f[i]] = A[f[i-1]]

        if W[f[i]] > max:
            a = f[i]
    return [W[a], A[a]]

        
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    s = [1,1,3,4]
    f = [2,4,4,5]
    w = [1,1,1,1]
    n = len(f)
    assert n == len(s)

    #schedule_rec = interval_scheduling_recursive(s, f, 0, n)
    #print(schedule_rec[:])

    #schedule_it = interval_scheduling_iterative(s, f, n)
    #print(schedule_it[:])

    schedule_weight = interval_scheduling_weighted(s, f, w, n)
    print(schedule_weight)
