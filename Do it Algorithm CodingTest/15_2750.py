import sys; input = sys.stdin.readline

def main() :
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    for i in range(N) :
        for j in range(i + 1, N) :
            if(nums[i] >= nums[j]) :
                nums[i], nums[j] = nums[j], nums[i]
    for i in nums :
        print(i)
        

main()