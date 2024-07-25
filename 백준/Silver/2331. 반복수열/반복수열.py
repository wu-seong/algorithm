import sys
input = sys.stdin.readline

visited = []
def repeated_seq(A,P):
    visited.append(A)
    transfered = transfer(A, P) 
    while transfered not in visited:
        visited.append(transfered)
        transfered = transfer(transfered, P)
    return transfered


def transfer(num, power):
    sum = 0
    str_num = str(num)
    for part_num in str_num:
        sum += (int)(part_num)**power
    return sum


A, P = map(int, input().rstrip().split())

repeated_start_num = repeated_seq(A, P)
start_index = visited.index(repeated_start_num)
print("%d\n" %(start_index))

