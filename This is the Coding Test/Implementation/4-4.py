'''
★예제 4-4 게임 개발★
전형적인 시뮬레이션 문제. 삼성전자 공채 코딩 테스트에서 자주 출제되는 대표적인 유형이다.
문제가 길고 문제를 바르게 이해하여 소스코드로 옮기는 과정이 간단하지 않다.
따라서 이러한 문제를 잘 풀 수 있도록 반복적인 숙달이 필요하다.
'''
# 4-4
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
  # 왼쪽으로 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1
  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 이동하기
    if array[nx][ny] == 0:
      x = nx
      y = ny
      # 뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0

print(count)

'''
문제 풀이를 위한 중요한 테크닉을 다시 설명하자면, 일반적으로 방향을 설정해서
이동하는 문제 유형에서는 dx, dy라는 별도의 리스트를 만ㄷ르어 방향을 정하는 것이 효과적이다.
예를 들어 다음의 답안 예시 코드에서는 현재 캐릭터가 북쪽을 바라보고 있을 때 북쪽으로 이동하기
위해 x와 y좌표를 각각 dx[0], dy[0]만큼 더한다. 다시 말해서 현재 위치에서 (-1, 0)만큼
이동시키는 것이다. 이처럼 코드를 작성하면, 반복문을 이용하여 모든 방향을 차례대로
확인할 수 있다는 점에서 유용하다. 떠힌 2차원 리스트를 초기화할 때는 컴프리헨션을 이용하는 것이
효율적이다.

보통 실무의 코딩은 예외를 고려해서 코드를 짜야 하지만, 코딩 테스트는 입력값이 주어지는
경우가 대부분이므로, 이런 예외처리를 고려하지 않고 빠르게 코드를 작성하는 데 목표를 둔다.
'''