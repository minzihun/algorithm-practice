'''
★기출 06. 무지의 먹방 라이브★
회전판에 먹어야 할 n개의 음식이 있습니다.
각 음식에는 1부터 n까지 번호가 붙어있으며, 각 음식을
섭취하는데 일정 시간이 소요됩니다. 무지는 다음과 같은 방법으로 음식을 섭취합니다.
1. 무지는 1번 음식부터 먹기 시작하며,
   회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓습니다.
2. 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 옵니다.
3. 무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취합니다.
   다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말합니다.
4. 회전판이 다음 음식을 무지 앞으로 가져오는 데 걸리는 시간은 없다고 합니다.
무지마 먹방을 시잔한지 k초 후에 네트워크 장애로 인해 방송이 잠시 중단되었습니다. 무지는
네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지를 알고자 합니다.
각 음식을 모두 먹는데 필요한 시간이 담겨 있는 배열 food_times, 네트워크 장애가 발생한
시간 k초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return 하도록
solution 함수를 완성하세요.

내가 생각한 것보다 더 많이 생각해야 문제를 풀 수 있었다... 꼭 다시 풀어볼 수 있어야겠다.
카카오 같은데 들어 가려면 이 정도 문제는 구현할 수 있어야겠지? 화이팅.. 시작이 반이다:))

해설지를 보면 시간이 적게 걸리는 음식부터 확인하는 탐욕적 접근 방식으로 해결할 수 있다.
모든 음식을 시간을 기준으로 정렬한 뒤에, 시간이 적게 걸리는 음식부터 제거해 나가는 방식을
이용하면 된다. 이를 위해 우선순위 큐를 이용하여 구현할 수 있는데 ,문제를 풀기 위해 고려해야 하는
부분이 많아서 까다로울 수 있다. 자세한 설명은 해설지를 참고해야겠다...ㅇㅏㅏㅏ 봐도 이해가 안됭..
'''
# A06
# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    q = [] # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))
    
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    
    length = len(food_times) # 남은 음식의 개수
    
    # sum_value + (현재의 음식 시간 - 이전의 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정
    
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key =lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]

'''
내가 생각했을 때는 전체 요리개 몇 가지인 지 먼저 파악한 후에,
모든 요리의 시간이 0이면 멈추고 -1를 반환하고 아니면, 계속 돌면서
음식의 시간을 1씩 지워주면서 다음 위치를 i로 표시하고 멈추고 다시 시작할 때
그 k만 반환해주는 코드를 짜고 싶은데 생각만큼 쉽지가 않네?

# 내가 푼 코드
food_times = [3, 1, 2]
k = 5
total = 0

for _ in food_times:
  total += 1

i = 0

def solution(k):
  while True:
    if i > total: i = 0
    if food_times.count(0) == total: return -1
    if food_times[i] == 0:
      i += 1
      continue
    else: food_times[i] -= 1
    i += 1
    k -= 0
    if k == 0: return print(i)
'''