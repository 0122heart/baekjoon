def main() :
    N = int(input())
    An = list(map(int, input().split()))
    
    # 오름차순 정렬
    An.sort()

    # 찾을 값들
    M = int(input())
    target = map(int, input().split())

    # 차례로 이진탐색 시행
    for i in target :
        print(binarySearch(i, An))

def binarySearch(num, An) :
    start = 0
    end = len(An)

    while(end - start != 1) :
        mid = (start + end) // 2

        # 목표 값이 기준 값보다 작을 때
        if(num < An[mid]) :
            end = mid

        # 목표 값 발견
        elif(num == An[mid]) :
            return 1
        
        # 목표 값이 기준 값보다 클 때
        else :
            start = mid

    if(end - start) : 
        if(An[end - 1] == num) : return 1
    
    # 목표 값이 없을 때
    return 0

main()