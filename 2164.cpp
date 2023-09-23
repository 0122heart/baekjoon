#include <iostream>
#include <queue>

using namespace std;


void f_throwAwayCard(queue<int>& cards){
    cards.pop();
}

void f_toBottom(queue<int>& cards){
    cards.push(cards.front());
    cards.pop();
}

int main() {
    int num_card;
    cin >> num_card;

    queue<int> cards;

    for(int i = 1; i < num_card + 1; i++){
        cards.push(i);
    }

    while(1 < cards.size()){
        f_throwAwayCard(cards);
        f_toBottom(cards);
    }

    cout << cards.front();

    return 0;
}
