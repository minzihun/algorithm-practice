'''
예제 3-2 큰 수의 법칙
가장 큰 수와 두 번째로 큰 수를 생각하면 되는 문제다.
가장 큰 수는 k번, 두 번째로 큰 수는 1번을 m번 더해지는 과정이다.
이렇게 반복문을 짜도 되지만 그렇게 되면 데이터의 양이 많아지면
시간 초과로 초래될 수 있다. 그래서 책의 해설에서는 효율성을 찾으란다.
k번 + 1번의 과정이 일렬의 수열. 수열을 이용해서 코드를 작성하였다.
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 입력받은 데이터를 오름차순으로 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

count = int(m / (k + 1)) * k # K+1이라는 수열이 반복된 횟수
count += m