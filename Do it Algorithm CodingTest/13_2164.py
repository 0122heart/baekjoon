import sys; input = sys.stdin.readline
from collections import deque

def main() :
    numCard = int(input())
    cards = deque()
    
    # 초기 설정
    for i in range(numCard) :
        cards.append(i + 1)

    # 작업 실행
    while(1 < len(cards)) :
        cards.popleft()
        cards.append(cards.popleft())

    print(cards[0])

main()