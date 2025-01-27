'''
위치가 가장 낮은 순서부터 오른쪽 최대 도달지점을 구하기
오른쪽 최대 도달 지점 중에서 가장 작은 지점을 구하기
현재의 왼쪽 최대 도달 지점 > 현재까지 구한 오른쪽 최대 도달 지점의 최솟값 이면 -> 한 점에서 만날 수 없다.
-> 0
현재의 오른쪽 최대 도달 지점 < 현재까지 구한 오른쪽 최대 도달 지점의 최솟값-> 현재까지 구한 오른쪽 최대 도달 지점 최솟값 갱신

모든 점까지 순회를 완료했으면
-> 1
'''

def calculate(num):
    num = int(num)
    return num * T
import sys
input = sys.stdin.readline

def transfer(num):
    return int(float(num)*1e4)

N, T = map(transfer, input().rstrip().split())

location = list(map(int, input().rstrip().split()))
for i in range(len(location)):
    location[i] *= 1e4
move_distance = list(map(calculate, input().rstrip().split()))
#print(location, move_distance)

min_end = float('inf')

student = list(zip(location, move_distance))
student.sort(key=lambda x: x[0])
#print(student)

for l, m in student: 
    if l-m > min_end:
        print(0)
        exit()
    if l+m < min_end:
        min_end = l+m
print(1)