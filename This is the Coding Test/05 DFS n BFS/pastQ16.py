'''
★기출 16. 연구소★
연구소의 크기가 N x M인 직사각형으로 나타낼 수 있으며, 직사각형은 1 x 1 크기의 정사각형으로
나누어져 있습니다. 연구소는 빈칸, 벽으로 이루어져있으며, 벽은 칸 하나를 가득 차지합니다.
일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수
있습니다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 합니다.
0은 빈칸, 1은 벽, 2는 바이러스가 있는 곳입니다. 아무런 벽을 세우지 않는다면, 바이러스는 모든
빈칸으로 퍼져나갈 수 있습니다. 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고
합니다. 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을
작성하세요. 바이러스(2)의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수입니다.
빈칸(0)의 개수는 3개 이상입니다.
모든 조합을 계산할 때는 파이썬의 조합 라이브러리를 이용하거나, DFS 혹은 BFS를 이용하여
해결할 수 있다. 따라서 벽의 개수가 3개가 되는 모든 조합을 찾은 뒤에 그러한 조합에 대해서
안전 영역의 크기를 계산하면 된다. 안전 영역의 크기를 구하는 것 또한 DFS나 BFS를 이용하여
계산할 수 있다. 결과적으로 여기서는 가능한 모든 경우의 수를 계산하되, 안전 영역을 계산할 때
DFS 혹은 BFS를 실수 없이 구현해야 정답 판정을 받을 수 있다. 문제 풀이 아이디어를 간략히
설명하면, 초기에 비어 있는 모든 공간 중에서 3개를 골라 벽을 설치하는 것이다. 매번 벽을 설치할
때마다, 각 바이러스가 사방으로 퍼지는 것을 DFS/BFS로 계산하여 안전 영역을 구해야 한다.
'''
# A16
n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
  data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      if temp[nx][ny] == 0:
        # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
        temp[nx][ny] = 2
        virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계한하는 메서드
def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
  global result
  # 울타리가 3개 설치된 경우
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j]
    # 각 바이러스의 위치에서 전파 진행
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i, j)
    # 안전 영역의 최댓값 계산
    result = max(result, get_score())
    return
  # 빈 공간에 울타리 설치
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        data[i][j] = 0
        count -= 1

dfs(0)
print(result)
