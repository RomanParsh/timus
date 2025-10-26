from collections import deque
import sys


def bfs(n, adj, start):
	dist = [-1] * n
	dq = deque()
	dist[start] = 0
	dq.append(start)
	while dq:
		u = dq.popleft()
		for v in adj[u]:
			if dist[v] == -1:
				dist[v] = dist[u] + 1
				dq.append(v)
	return dist


def main():
	line = input().strip()
	while line == '':
		line = input().strip()
	n, m = map(int, line.split())
	adj = [[] for _ in range(n)]
	for _ in range(m):
		a, b = map(int, input().split())
		a -= 1
		b -= 1
		adj[a].append(b)
		adj[b].append(a)
	s, f, r = map(int, input().split())
	s -= 1
	f -= 1
	r -= 1

	ds = bfs(n, adj, s)
	df = bfs(n, adj, f)
	dr = bfs(n, adj, r)

	D = ds[f]


	on_short = [False] * n
	for i in range(n):
		if ds[i] != -1 and df[i] != -1 and ds[i] + df[i] == D:
			on_short[i] = True

	out = [[] for _ in range(n)]
	layers = [[] for _ in range(D + 1)]
	for u in range(n):
		if not on_short[u]:
			continue
		layers[ds[u]].append(u)
		for v in adj[u]:
			if on_short[v] and ds[u] + 1 == ds[v]:
				out[u].append(v)
	dp = [-1] * n
	for layer in range(D, -1, -1):
		for u in layers[layer]:
			if not out[u]:
				dp[u] = dr[u]
			else:
				best = -1
				for v in out[u]:
					if dp[v] > best:
						best = dp[v]
				dp[u] = min(dr[u], best)

	print(dp[s])


if __name__ == '__main__':
	main()

