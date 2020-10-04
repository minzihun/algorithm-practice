'''
예제 4-2 시각
시/분/초를 문자로 한 리스트에 넣어서 각각의 숫자가 한 원소가 되게해
count 함수 이용해 그 중에 n이라는 원소가 있을 때마다 count 변수에 추가해
기록했다. 3중 반복문을 이용해 문제를 풀었다.

'''
# 내가 푼 코드
n = int(input())

# 정답 대로 하면 이렇게 굳이 시/분/초 리스트를 만들어서 메모리 낭비할 일 안 만들었을텐데
# 어잡히 분/초는 59분/49초까지니깐 따로 만들 필요는 없었다. 
h = [i for i in range(n+1)]
m = [i for i in range(60)]
s = [i for i in range(60)]

now = 0 # 조건문 in을 이용하면 현재시간을 담을 변수도
count = 0

for hh in h:
  for mm in m:
    for ss in s:
      # 그 변수에 현재 시간을 리스트로 넣어서 count 함수를 이용하는 일도 없었다.
      now = list(str(hh)+str(mm)+str(ss))
      if now.count('3') >= 1:
        count += 1
# 확실해 답안 코드가 더 효율적이고 메모리 사용이 효율적인 것 같다.
print(count)

'''
이러한 유형은 완전 탐색유형으로 분류되기도 한다.
완전 탐색 알고리즘은 가능한 경우의 수를 모두 검사해보는 탐색 방법이다.
완전 탐색 알고리즘은 비효율적인 시간 복잡도를 가지고 있으므로 데이터
개수가 큰 경우에 정상적으로 동작하지 않을 수 있다. 그래서 일반적으로
알고리즘 문제를 풀 때는 확인해야 할 전체 데이터의 개수가 100만개 이하일 때
완전 탐색을 사용하면 적절하다.

나는 count라는 list함수를 이용했지만 답안 코드에서는 조건문의 in 기능을 활용했다.
# 4-2
h = int(input())

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(k) + str(k):
        count += 1

print(count)
'''