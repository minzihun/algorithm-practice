'''
예제 3-5 1이 될 때까지
최대한 많이 나누기를 하면 된다.
k가 2이상의 자연수이면 나누는 것이 항상 1빼는 것보다 유리하다.
이 문제도 3-2.py와 마찬가지로 내가 작성한 코드가 더 직관성이 높지만,
해설에 따라 더 빠르게 코드가 작동하려면 n이 k의 배수가 되록 하는
효율적으로 한 번에 빼는 방식의 소스코드를 작성할 수 있다.
'''
# 3-6
n, k = map(int, input().split())
result = 0

while True:
  target = (n // k) * k # target은 k로 나눠지는 수, 즉 k의 배수
  result += (n - target) # n - k의 배수 = 1씩 빼야하는 횟수, 뺀 횟수 만큼 result에 넣어주고
  n = target # n을 k의 배수로 셋팅
  if n < k: # n이 k보다 작아지면 나누질 못하니깐 while문 빠져나간다.
    break
  result += 1 # 횟수에 1 추가하고
  n //= k # 다시 한번 나눈다~ 그리고 이 과정을 n이 k보다 작아질 때까지 반복한다.

result += (n - 1)
 # n이 1이 될때 까지니깐 남은 수 모두는 무조건 빼져야되니 그 수만큼 result에 더한다.
print(result)

'''
# 내가 푼 코드
n, k = map(int, input().split())
result = 0

while n > 1:
  if n % k == 0: # n이 k로 나눠떨어지면 나누기
    n /= k
    result += 1
  else: # 나눠떨어지지 않는 다면 빼세요!
    n -= 1
    result += 1

print(result)
'''