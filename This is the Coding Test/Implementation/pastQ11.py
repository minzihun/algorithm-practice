'''
★기출 11. 뱀★
Dummy라는 도스 게임이 있는데, 뱀이 나와 기어 다니는데, 사과를 먹으면 뱀의 길이가 늘언다.
뱀이 이리저리 기어 다니다가 벽 또는 자신의 몸과 부딪히면 게임이 끝난다.
게임은 N x N 정사각 보드 위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다.
보드의 테두리는 벽이다. 게임을 시작할 때 뱀은 맨 위 맨 좌측에 위치하고 뱀의 길이는 1이다.
뱀은 처음에 오른쪽을 향한다. 뱀은 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
 - 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다.
 - 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
 - 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
   즉, 몸길이는 변하지 않는다.

이 문제 또한 전형적인 시뮬레이션 문제 유형이다. 2차원 배열상의 맵에서 뱀이 이동하도록
해야 하므로 2차원 배열상의 특정 위치에서 동, 남, 서, 북의 위치로 이동하는 기능을
구현해야 한다. 이 준제의 경우, 뱀이 처음에 동쪽을 바라보고 있다는 점을 고려하자.
뱀의 머리가 뱀의 몸에 닿는 경우에도 종료해야 하므로, 매 시점마다 뱀이 존재하는 위치를
항상 2차원 리스트에 기록해야한다. 이런 시뮬레이션 문제 유형을 가장 쉽게 풀기 위해서는
그림으로 그려 보는 것이 좋다. 일반적인 코딩 테스트에서는 종이와 펜은 사용하게 해준다.
'''
# A11
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
  a, b = map(int, input().split())
  data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
  x, c = input().split()
  info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
  if c == "L":
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4
  return direction

def simulate():
  x, y =1, 1 # 뱀의 머리 위치
  data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
  direction = 0 # 처음에는 동쪽을 보고 있음
  time = 0 # 시작한 뒤에 지난 '초' 시간
  index = 0 # 다음에 회전할 정보
  q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
      # 사과가 없다면 이동 후에 꼬리 제거
      if data[nx][ny] == 0:
        data[nx][ny] = 2
        q.append((nx, ny))
        px, py = q.pop(0)
        data[px][py] = 0
      # 사과가 있다면 이동 후에 꼬리 그대로 두기
      if data[nx][ny] == 1:
        data[nx][ny] = 2
        q.append((nx, ny))
    # 벽이나 뱀의 몸통과 부딪혔다면
    else:
      time += 1
      break
    x, y = nx, ny # 다음 위치로 머리를 이동
    time += 1
    if index < 1and time == info[index][0]: # 회전할 시간인 경우 회전
      direction = turn(direction, info[index][1])
      index += 1
  return time

print(simulate())

'''
지지 쳤어욤ㅠㅠ 너무 어렵다.
# 내가 푼 코드
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
  '''