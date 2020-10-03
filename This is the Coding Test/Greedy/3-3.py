'''
예제 3-3 숫자 카드 게임
카드가 n * m 형태로 놓여 있는 데
행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 한다.
자신이 속한 행에서는 가장 작으나 각 행의 최소 숫자중에서 가장 큰 수는?
이라고 묻는 문제이다. 카드 받아서 섞지 않는다면 처음 받을 때부터 한 행에
최솟값만 리스트에 넣어주면 나중에 그 값들 중 가장 큰 값만 찾으면 답이아닐까?
그럼 코드가 짧아지지 않을 까 생각했다. 처음에는 arr 리스트를 초기화 시키놓지
않아 IndexError: list assignment index out of range 메시지가 떳지만
입력한 행만큼 리스트를 초기화 시켜 놓아 이를 해결 했다.
'''

n, m = map(int, input().split())
arr = [0 for _ in range(n)]

for i in range(n):
  arr[i] = min(list(map(int, input().split())))

result = max(arr)
print(result)

'''
책에나온 답안 2가지

- min() 함수를 이용하는 경우
n, m = map(int, input().split())
result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data) # 나는 이 부분이 괜히 변수 선언을 하는 느낌?
  result = max(result, min_value) # 이것도 굳이 result를 0으로 두고 비교 해야되나?

print(result)

- 2중 반복문 구조를 이용하는 경우
n, m = map(int, input().split())
result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = 10001 # 각 숫자는 0이상 10000이하라는 것을 이용해 변수 이용한 듯
  for a in data: # 한 줄에 입력받은 데이터 m개를 비교해 젤 작은 것만 변수 넣어준다.
    min_value = min(min_value, a)
  result = max(result, min_value) # 이렇게 n번 반복해 젤 큰 값이 result에 들어간다.

print(result)
'''