'''
예제 3-1 거스름돈
큰 단위의 화폐부터 거슬러 주기.
큰 단위화폐가 항상 작은 단위의 배수가 된다.
작은 단위화폐를 종합해 다른 해가 나올 수 없다.
'''

n = 1260
count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n//coin
  n %= coin

print(count)