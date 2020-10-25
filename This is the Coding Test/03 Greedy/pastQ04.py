'''
기출 04. 만들 수 없는 금액
동빈이는 n개의 동전을 가지고 있는데, 이때 n개의 동전을 이용하여
만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하세요.
itertools 라이브러리를 불러와 combinations 함수를 이용화면 되지 않을까 하는 생각.
몇개씩 뽑냐는 1부터 전체 수 만큼으로 하면 되겠죠?
그 모든 조합들에 map함수 이용해서 sum함수 적용하고 그거를 다시 차례대로 나열해서
그 수를 1부터 하나씩 올라가면서 비교해서 1부터 올린 수는 있는데 리스트에 없으면
그 값이 답이 되지 않을 까? 라고 생각했다.

일단 동전에 대한 정보가 주어졌을 때, 화폐 단위 기준으로 오름차순 정렬한다.
이후에 1부터 차례대로 특정 금액을 만들 수 있는지 확인하면 된다.
1부터 target-1까지의 모든 금액을 만들 수 있다고 가정해보자.
우리는 화폐 단위가 작은 선수대로 동전을 확인하며, 현재 확인하는 동전을 이용해
target 금액 또한 만들 수 있는지를 화깅ㄴ하면 된다.
만약 target 금액을 만들 수 있다면, target 값을 업데이트하는 방식을 이용한다. 

나는 화폐단위로만 생각 한 것 자체가 오류다 왜냐면 동전이 여러개 있는 건데
그 동전들을 더할 생각을 해야되는데 지금 있는 화폐 단위들의 조합만 생각한게
오류 인 것 같다. 그래서 이 문제는 해설지의 코드를 참고하고 다시 풀어보면 좋을 것 같다.
'''
# A04
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1 # 처음에 금액 1을 만들 수 있는지 확인하기 위해 target을 1로 한다.
for x in data:
  if target < x:
  # 만들 수 없는 금액을 찾았을 떄 반복 종료
  # target이랑 x랑 같은 게 조건이 아닌 target보다 작은게 조건이니,
  # 그 뜻은 target이하의 수는 지금 x자리 이하의 요소 조합으로 만들 수 있다는 뜻!
    break
  target += x

print(target)

'''
# 내가 푼 코드
from itertools import combinations

n = int(input())
coin_lists = list(map(int, input().split()))
coin_sum = list()
coin_combinations = list()
for i in range(1, n+1):
  coin_sum.append((map(sum, combinations(coin_lists, i)))
  # 여기서 리스트 형태로 리스트에 저장되는 게 이걸 한 개씩 저장하고 싶고,
  # 그렇게 저장후에 중복 제대하고 오름차순 나열해서 1이랑 비교하고 싶은데..  뜻대로 안됨ㅋㅋ
'''