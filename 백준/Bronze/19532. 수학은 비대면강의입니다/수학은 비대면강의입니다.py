import sys
print = sys.stdout.write
input = sys.stdin.readline

a,b,c,d,e,f = map(int, input().rstrip().split())

origin_a = a
origin_b = b
origin_c = c
origin_d = d
origin_e = e
origin_f = f

a *= d
b *= d
c *= d

d *= origin_a
e *= origin_a
f *= origin_a

y = (c-f)/(b-e)
if origin_a == 0:
    x = (origin_f-(origin_e*y)/origin_d)
    print("%d %d\n" %(x, y))
    exit()
x = (origin_c-(y*origin_b))/origin_a

print("%d %d\n" %(x, y))