import sys

input = sys.stdin.readline
numMaterial = int(input())
target = int(input())
materials = list(map(int, input().split()))

def main() :
    # 오름차순으로 정렬
    materials.sort()
    # 만족하는 조합의 개수
    satisfying = 0
    start, end = 0, numMaterial - 1
    while(start < end) :
        sumNumbers = materials[start] + materials[end]
        # 만족
        if(sumNumbers == target) :
            satisfying += 1
            start += 1; end -= 1
        # 작을 때 -> 더 키워야 함
        elif(sumNumbers < target) :
            start += 1
        # 클 때 -> 더 줄여야 함
        else :
            end -= 1
    print(satisfying)

main()