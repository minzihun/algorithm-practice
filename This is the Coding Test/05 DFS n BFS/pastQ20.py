'''
★기출 20. 감시 피하기★
N * N 크기의 복도가 있습니다. 특정한 위치에는 선생님, 학생, 혹은 장애물이 있습니다.
현재 학생 몇 명이 수업 시간에 몰래 복도에 나왔는데, 복도에 나온 학생들이 선생님의 감시에
들키지 않는 것이 목표입니다. 각 선생님은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로
감시를 진행합니다. 단, 복도에 장애물이 있으며 선생님은 장애물 뒤편에 숨어 있는 학생을 볼 수
없습니다. 또한 선생님은 시력이 매우 좋아 아무리 멀리 있더라도 장애물로 막히기 전까지 4가지
방향으로 학생을 모두 볼 수 있다고 합니다. 문제에서 위칫값을 나타낼 때는 (행, 열)의 형태로
표현합니다. 각 칸은 선생님이 존재하면 T, 학생이 존재하면 S, 장애물이 존재하면 O로 표시합니다.
학생들은 복도의 빈칸 중에서 장애물을 설치할 위치를 골라, 정확히 3개의 장애물을 설치해야 합니다.
그리고 장애물을 3개 설치해서 선생님의 감시로부터 모든 학생이 피할 수 있는지 계산해야 합니다.
N * N 크기의 복도에서 학생과 선생님의 위치 정보가 주어졌을 때, 장애물을 정확히 3개 설치하여
모든 학생이 선생님의 감시를 피할 수 있는지 출력하는 프로그램을 작성하세요.

이 문제는 장애물을 정확히 3개 설치하는 모든 경우를 확인하여, 매 경우마다 모든 학생을 감시로부터
피하도록 할 수 있는지의 여부를 출력해야 한다. 모든 조합을 찾기 위해서 DFS 혹은 BFS를 이용해
모든 조합을 반환하는 함수를 작성하거나, 파이썬의 조합 라이브러리를 이용할 수 있다. 또한 정확히
3개의 장애물이 설치된 모든 조합마다, 선생님들의 위치 좌표를 하나씩 확인하고 각각 선생님의
위치에서 상, 하, 좌, 우를 확인하며 학생이 한 명이라도 감지되는지를 확인해야한다. 이는 별도의
watch() 메서드를 구현하면 편하다. 문제 풀이는 파이썬의 조합 라이브러리를 이용하여 DFS/BFS를
대체하였다.
'''
# A20
from itertools import combinations

n = int(input()) # 복도의 크기
board = [] # 복도 정보(N x N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
  board.append(list(input().split()))
  for j in range(n):
    # 선생님이 존재하는 위치 저장
    if board[i][j] == 'T':
      teachers.append((i, j))
    # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
    if board[i][j] == 'X':
      spaces.append((i, j))

# 특정 방향으로 감시를 진행(학생 발견: True, 학생 미발견: False)
def watch(x, y, direction):
  # 왼쪽 방향으로 지시
  if direction == 0:
    while y >= 0:
      if board[x][y] == 'S': # 학생이 있는 경우
        return True
      if board[x][y] == 'O': # 장애물이 있는 경우
        return False
      y -= 1
  # 오른쪽 방향으로 감시
  if direction == 1:
    while y < n:
      if board[x][y] == 'S': # 학생이 있는 경우
        return True
      if board[x][y] == 'O': # 장애물이 있는 경우
        return False
      y += 1
  # 위쪽 방향으로 감시
  if direction == 2:
    while x >= 0:
      if board[x][y] == 'S': # 학생이 있는 경우
        return True
      if board[x][y] == 'O': # 장애물이 있는 경우
        return False
      x -= 1
  # 아래쪽 방향으로 감시
  if direction == 3:
    while x < n:
      if board[x][y] == 'S': # 학생이 있는 경우
        return True
      if board[x][y] == 'O': # 장애물이 있는 경우
        return False
      x += 1
  return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
  # 모든 선생님의 위치를 하나씩 확인
  for x, y in teachers:
    # 4가지 방향으로 학생을 감지할 수 있는지 확인
    for i in range(4):
      if watch(x, y, i):
        return True
  return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
  # 장애물 설치해보기
  for x, y in data:
    board[x][y] = 'O'
  # 학생이 한 명도 감지되지 않는 경우
  if not process():
    # 원하는 경우를 발견한 것임
    find = True
    break
  # 설치된 장애물을 다시 없애기
  for x, y in data:
    board[x][y] = 'X'

if find:
  print('YES')
else:
  print('NO') 
  