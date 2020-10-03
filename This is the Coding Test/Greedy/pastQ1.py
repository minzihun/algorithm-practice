'''
기출 01. 모험가의 길드
n명의 모험가를 대상으로 공포도를 측정했는데,
공포도가 x인 모험가는 반드시 x명이상으로 구성한
모험가 그룹에 참여해야 모험을 떠날 수 있다.
최대 몇개의 모험가 그룹을 만들 수 있는가?
모험가들을 공포도 순으로 오름차순 정렬하고
공포도가 적은 순으로 끊어서 그룹 형성하면
가장 많은 모험가 그룹을 만들 수 있다고 생각해서
아래와 같은 코드를 작성했다.
'''
# 내가 푼 코드
n = int(input())
adventurers = list(map(int, input().split()))
adventurers.sort() # 공포도 기준으로 오름차순 정렬
result = 0
x = 0
 # 모험가 그룹의 인덱스 역할을 하면서 공포도가 몇 인지 파악하여 몇명 까지 모아야되는지 계산

while x < len(adventurers):
 # 모험가의 인덱스가 리스트의 길이보다 커버리면 더 이상 그룹 형성 안되잖아!!
  if x + adventurers[x] >= len(adventurers):
    # 위에 while문 통과했더라도
    # 빼낼 모험가의 수가 리스트의 길이 보다 커버리면 또 그룹 형성 못하니깐 while문 나간다.
    break
  else: #위에 두 조건에 해당안하면 그룹 만들고 result에 1더해준다~
    x += adventurers[x]
    result += 1

print(result)

'''
해설지 풀이도 나랑 거의 비슷한데 구현 방법이 조금 다르다. 해설지가 더 좋은 듯!
# A01
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
  count += 1 # 현재 그룹에 해당 모험가를 포함시키기
  if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    result += 1 # 총 그룹의 수 증가시키기
    count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력
'''