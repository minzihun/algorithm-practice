'''
★기출 12. 기둥과 보 설치★
죠르디는 기둥과 보를 이용하여 벽면 구조물을 자동으로 세우는 로봇을 개발할 계획인데,
그에 앞서 로봇의 동작을 시뮬레이션 할 수 있는 프로그램을 만들고 있습니다.
프로그램은 2차원 가상 벽면에 기둥과 보를 이용한 구조물을 설치할 수 있는데,
기둥과 보는 길이가 1인 선분으로 표현되며 다음과 같은 규칙을 가지고 있습니다.
 - 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야 한다.
 - 보는 한쪽 끝부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어야 한다.
2차원 벽면은 n x n 크기 정사각 격자 형태이며, 각 격자는 1 x 1 크기입니다. 맨 처음 벽면은
비어있는 상태입니다. 기둥과 보는 격자 선의 교차점에 걸치지 않고, 격자 칸의 각 변에 정확히
일치하도록 설치할 수 있습니다. 벽면의 크기 n, 기둥과 보를 설치하거나 삭제하는 작업이
순서대로 담긴 2차원 배열 build_frame이 매개변수로 주어질 떄, 모든 명령어를 수행한 후
구조물의 상태를 return 하도록 solution 함수를 완성해주세요.

전형적인 시뮬레이션 문제이다. 문제를 쉽게 해결하기 위한 아이디어를 머릿속으로 잘 정리한 뒤에
코드 작성을 시작해야한다. 일단 요구사항을 확인해보면, 전체 명령의 개수는 총 1,000개 이하이다.
전체 명령의 개수를 M이라고 할 때, 시간 복잡도 O(M**2)으로 해결하는 것이 이상적일 것이다.
하지만 본 문제의 시간 제한은 5초로 넉넉한 편이므로 O(M**3)의 알고리즘을 이용해도 정답 판정을
받을 수 있다. 따라서 이 문제를 O(M**3)의 시간 복잡도로 해결하는 가장 간단한 방법은,
설치 및 삭제 연산을 요구할 때마다 일일이 '전체 구조물을 확인하며' 규칙을 확인하는 것이다.
아래 소스코드에서는 possible() 메서드를 이용하여 현재의 구조물이 정상인지를 체크할 수 있도록
하였다. 그래서 매번 연산이 발생할 때마다, possible() 함수를 호출하여 현재 구조물이 정상인지를체크하고, 정상이 아니라면 현재의 연산을 무시하도록 한다.
'''
# A12
# https://programmers.co.kr/learn/courses/30/lessons/60061

# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝 부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False # 아니라면 거짓(False) 반환
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False # 아니라면 거짓(False) 반환
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame: # 작업(frame)의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 가능한 구조물이 아니라면 다시 설치
        if operate == 1: # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니라면 다시 제거
    return sorted(answer) # 정렬된 결과를 반환