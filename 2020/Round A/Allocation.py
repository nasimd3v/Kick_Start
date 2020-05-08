https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56


def solve(case,have , h_list):
	ans= 0 
	avl =  have
	for house in sorted(h_list):
		if house > avl:
			break
		else:
			ans+= 1nn
			avl -= house	
	print("Case #{0}: {1}".format(case, ans))
			

if __name__ == '__main__':
	t = int(input())
	for case in range(1,t+1):
		have = list(map(int,input().split(" ")))[1]
		h_list = list(map(int,input().split(" ")))
		solve(case,have, h_list)
	
