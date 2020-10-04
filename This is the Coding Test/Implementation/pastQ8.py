'''
기출 08. 문자열 재정렬
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

이 문제는 파이썬 문법을 얼마나 알고 있냐가 핵심인 것 같다.
알파벳 대문자와 숫자로 구성된 문자열 입력 받아서 일단은 정렬해주면
문자는 알파벳 순으로 정렬 될 것이다. 여기서 리스트의 각각의 요소가
숫자면 따로 더하고 문자열 문자열에 알파벳 순으로 더해진다.
마지막에 출력할 때만 문자랑 숫자랑 합해서 출력해주면 된다!
'''
# 내가 푼 코드
s = list(input()) # 알파벳 대문자랑 숫자로 구성된 문자열을 입력 받아 리스트에 넣는다.
s.sort()
total = 0
string = ''

for i in s:
  if i.isdigit() == True :
    # 숫자면 total에 숫자를 더해준다. 정수로 바꿔서 해야겠죠~?
    total += int(i)
  else: string += i # 문자열 빈 문자열에 계속해서 더해준다. 이미 리스트 정렬했기에 알파벳순이다.

print(string + str(total)) # 더한 숫자만 문자열로 변환한 뒤 문자끼리 더해 출력해준다.

'''
# A07
data = input()
result = []
value = 0

for x in data:
  if x.isalpha():
    result.append(x)
  else:
    value += int(x)

result.sort()

if value != 0:
  result.append(str(value))

print(''.join(result))

정답 코드를 보면 isalpha()랑 join함수를 사용했다.
나는 join()함수의 기능을 몰랐다!
문자열 타입의 리스트가 있을 때 각 요소들을 하나의 문자열로 만들자고 할 때 사용할 수 있다.
result = ''.join(arr) 혹은 result = str.join('', arr) 두 가지 방법으로 사용 할 수 있다.
'''