#2
#2 4 5
#10 10 100 30
#80 50 10 50
#3 2 3
#80 80
#15 50
#20 10
def solve(N, K, P, A):
    prefixes = []
    for row in A:
        pre_fixes = [0]
        for x in row:
            pre_fixes.append(pre_fixes	[-1] + x)
        prefixes.append(pre_fixes)
    cash = {}
    def dp(i, take):
        if take == 0 or i == N:
            return 0
        if (i, take) in cash:
            return cash[i, take]
        ans = 0
        for choice in range(K+1):
            take2 = take - choice
            if take2 < 0: break
            cand = dp(i+1, take2) + prefixes[i][choice]
            if cand>ans:ans=cand
        cash[i, take] = ans
        return ans
    return dp(0, P)


if __name__ == '__main__':
	t = int(input())
	for case in range(1,t+1):
		n , k , p = list(map(int, input().split(" ")))
		a = [list(map(int,input().split(" "))) for _ in range(n)]
		ans = solve(n ,k ,p , a)
		print(f"Case #{case}: {ans}")
		

