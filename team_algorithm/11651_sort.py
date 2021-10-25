import sys
N = int(sys.stdin.readline()) arr = [] for i in range (N): (a,b) = map(int,sys.stdin.readline().split()) arr.append((b, a)) #리스트 정렬 사용 시, 튜플 안의 앞에 숫자를 우선으로 비교 한 다음 뒤의 숫자를 비교함. #우리는 y좌표를 우선으로 비교해야 하므로, 일단 x좌표 위치와 와 y좌표 위치를 바꿈 arr.sort() for i in range (len(arr)): print("%d %d"%(arr[i][1],arr[i][0])) # 위에서 x좌표와 y좌표 위치를 바꿨으므로 출력 시 다시 바꿔줌.
