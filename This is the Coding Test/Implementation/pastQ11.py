'''
기출 11. 뱀
Dummy라는 도스 게임이 있는데, 뱀이 나와 기어 다니는데, 사과를 먹으면 뱀의 길이가 늘언다.
뱀이 이리저리 기어 다니다가 벽 또는 자신의 몸과 부딪히면 게임이 끝난다.
게임은 N x N 정사각 보드 위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다.
보드의 테두리는 벽이다. 게임을 시작할 때 뱀은 맨 위 맨 좌측에 위치하고 뱀의 길이는 1이다.
뱀은 처음에 오른쪽을 향한다. 뱀은 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
 - 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다.
 - 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
 - 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
   즉, 몸길이는 변하지 않는다.
'''
# A11

n = int(input())
board = [[0] * n for _ in range(n)]
k = int(input())
count = 0
x, y = 0, 0

for _ in range(k):
  x, y = map(int, input().split())
  board[x-1][y-1] = 1

l = int(input())
directions = dict()
for i in range(l):
  key, val = input().split()
  directions[key] = val
print(directions)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

nx = 0
ny = 0
direction = 0
while True:
  if str(count) in directions:
    if directions[str(count)] == 'D':
      direction += 1
      if direction == 4:
        direction = 0
    else: direction -= 1
      if direction == -1:
        direction = 3
  
  nx += dx[direction]
  ny += ny[direction]

  if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= n-1:
    if board[nx][ny] == 1:
      board[nx][ny] = 0
      

  if board[i][j]