'''
예제 3-5 1이 될 때까지
최대한 많이 나누기를 하면 된다.
k가 2이상의 자연수이면 나누는 것이 항상 1빼는 것보다 유리하다.
이 문제도 3-2.py와 마찬가지로 내가 작성한 코드가 더 직관성이 높지만,
해설에 따라 더 빠르게 코드가 작동하려면 n이 k의 배수가 되록 하는
효율적으로 한 번에 빼는 방식의 소스코드를 작성할 수 있다.
'''

n, k = map(int, input().split())
result = 0

while True:
  target = (n // k) * k
  result += (n-target)
  n = target
  if n < k:
    break
  result += 1
  n //= k

result += (n - 1)
print(result)


'''
- 내가 푼 코드
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