
def compute(array, target):
    a=0
    b=len(array)-1

    while(a < b):
        s = array[a] + array[b]
        if s == target:
            break
        elif s > target:
            b-=1
        else:
            a+=1

    if a == b:
        return -1, -1
    else:
        return a, b

target = int(input())
array = list(map(int, input().split()))

print(compute(array, target))