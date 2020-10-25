'''
기출 07. 럭키 스트레이트
현재 캐릭터의 점수를 n이라고 할 때 자릿수를 기준으로 점수 n을 반으로
나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을
더한 값이 동일한 상황을 의미합니다. 현재 점수 n이 주어지면 럭키 스트레이트를
사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하세요.

구현하기 너무 쉬운 문제였다. 설명 생략..
'''
# 내가 푼 코드
n = input()
total = len(n)
score = [int(e) for e in n]
left, right = 0, 0

for i in range(total):
  if i < total/2:
    left += score[i]
  else:
    right += score[i]

if left == right: print("LUCKY")
else: print("READY")

'''
# A07
n = input()
length = len(n)
summary = 0

for i in range(length // 2):
  summary += int(n[i]) # 왼쪽 부분의 값은 더하고

for i in range(length // 2, length):
  summary -= int(n[i]) # 오른쪽 부분의 값은 빼고

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
  print("LUCKY")
else:
  print("READY")

해설지에서 작성한 코드가 가독성이 높고, 변수 사용도 줄어드는 것 같다!
'''