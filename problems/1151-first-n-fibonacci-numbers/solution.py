def first_n_fibonacci(n):
    if n ==0:
        return []
    elif n ==1:
        return [0]
    elif n ==2:
        return [0, 1]
    ans = [0,1 ]
    last=0
    for i in range(2, n):
        ans.append(ans[i-1]+ans[i-2])
    return ans