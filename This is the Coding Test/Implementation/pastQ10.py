'''
★기출 10. 문자열 압축★
자물쇠는 격자 한 칸의 크기가 1x1인 NxN 크기의 정사각 격자 형태이고
특이한 모양의 열쇠는 MxM 크기의 정사각 격자 형태로 되어 있습니다.
열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에
딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 자물쇠 영역 내에서는
열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며
열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 또한 자물쇠의 모든
홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.
열쇠를 나타내는 2차원 배열 key와 자물쇠를 나태내는 2차원 배열 lock이
매개볌수로 주어질 때 열쇠로 자물쇠를 열 수 있으면 true를, 열 수 없으면
false를 return 하도록 solution 함수를 완성해주세요.

자물쇠와 열쇠의 크기는 20*20보다 작다. 2차원 리스트에 있는 모든 원소에
접근할 때는 400만큼의 연산이 필요하다. 파이썬의 경우 일반적인 코테 채점 환경에서
1초에 2,000만에서 1억 정도의 연산을 처리할 수 있어서 완전 탐색을 이용해
모든 경우의 수를 해 볼 수 있다. 완전 탐색을 수월하게 하기 위해서
자물쇠 리스트의 크기를 3배 이상으로 변경하면 계산하기 수월해진다.
이제 배열은 왼쪽 위에서 시작해서 한 칸씩 이동하는 방식으로 차례대로
자물쇠의 모든 홈을 채울 수 있는지 확인하면 된다. 문제에서는 0은 홈 부분,
1은 돌기 부분을 나타낸다. 따라서 자물쇠 리스트에 열쇠 리스트의 값을 더한 뒤에,
더한 결과를 확인했을 때 자물쇠 부분의 모든 값이 정확히 1인지를 확인하면 된다.
'''
# A10
# https://programmers.co.kr/learn/courses/30/lessons/60059

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    
    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어가는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False