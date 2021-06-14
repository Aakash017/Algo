def Solve(N, A):
    c = A[0]
    for i in A:
        if i <= c:
            c = i
    return c
    # Write your code here


N = int(input())
A = list(map(int, input().split()))
out_ = Solve(N, A)
print(out_)
