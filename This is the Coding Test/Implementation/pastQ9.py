'''
★기출 09. 문자열 압축★
이 문제 또한 요구하는 대로 충실히 구현만 하면 정답 판정을 받을 수 있다.
입력으로 주어지는 문자열의 길이가 1,000 이하이기 때문에 가능한 모든 경우의 수를 탐색하는
완전 탐색을 수행할 수 있다. 길이가 n인 문자열이 입력되었다면 1부터 n/2까지의 모든 수를 단위로 하여
문자열을 압축하는 방법을 모두 확인하고, 가장 짧게 압축되는 길이를 출력하면 된다.

나는 이해가 잘 안된다... 구현 나에게 너무 먼 그... 더 열심히 노력해보자구~
'''
# A09
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
  answer = len(s)
  # 1개 단위(step)부터 압축 단위를 늘려가며 확인
  for step in range(1, len(s) // 2 + 1):
    compressed = ""
    prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
    count = 1
    # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
    for j in range(step, len(s), step):
      # 이전 상태와 동일하다면 압축 횟수(count) 증가
      if prev == s[j:j + step]:
        count += 1
      # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
      else:
        compressed += str(count) + prev if count >= 2 else prev
        prev = s[j:j + step] # 다시 상태 초기화
        count = 1
    # 남아 있는 문자열에 대해서 처리
    compressed += str(count) + prev if count >= 2 else prev
    # 만들어지는 압축 문자열이 가장 짧은 것이 정답
    answer = min(answer, len(compressed))
  return answer