import sys
N = int(sys.stdin.readline())
arr = [sys.stdin.readline() for _ in range(N)]
sys.stdout.write(''.join(map(str, sorted(arr))))
