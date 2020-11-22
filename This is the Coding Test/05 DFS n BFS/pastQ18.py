'''
★기출 18. 괄호 변환★
대부분 소스코드 내 작성된 괄호가 개수는 맞지만 짝이 맞지 않은 형태로 작성되어 오류가 나는 것을
알게 되었습니다. "콘"은 소스코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열을
알려주는 프로그램을 다음과 같이 개발하려고 합니다. '('와 ')'로만 이루어진 문자열이 있을 경우, 양
괄호의 개수가 같다면 이를 균형잡힌 괄호 문자열이라고 부릅니다. 그리고 여기에 '('와 ')'의 괄호의
짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열이라고 부릅니다. 균형잡힌 괄호 문자열 p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 "올바른 괄호 문자열"로 변환한 결과를 return 하도록
solution 함수를 완성해주세요.
이 문제는 제시된 알고리즘을 재귀적으로 구현하여 해결할 수 있다. 구현을 위한 알고리즘 자체는
문제에 그대로 제시되어 있기 때문에, 재귀 함수를 이용하여 문제에 기재되어 있는 알고리즘을
실수없이 안정적으로 구현할 수 있으며 문제를 해결할 수 있으면 문제를 해결할 수 있다.
엄밀히 말하면 이 문제는 DFS 문제는 아니다. 정확한 구현을 요구하고, 실수하기 쉬운 문제라는 점에서
DFS 연습 목적의 문제로 DFS/BFS 파트에서 다루고자 한다. 실수없이 풀라면 소스코드를 최대한 단순화
하는 것이 좋다. 따라서 특정 문자열에서 "균형잡힌 괄호 문자열"의 인덱스를 반환하는 함수와 특정한
"균형잡힌 괄호 문자열"이 "올바른 괄호 문자열"인지 판단하는 함수를 별도로 구현한다. 이후에
재귀함수에서 이 두 함수를 불러오도록 소스코드를 작성할 수 있다.
'''
# A18
# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3#

# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
        
# "올바른 괄호 문자열"인지 판단
def check_proper(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in  p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True # 쌍이 맞는 경우에 True 반환

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer