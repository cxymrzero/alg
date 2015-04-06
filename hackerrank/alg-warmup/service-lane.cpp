#include <iostream>

using namespace std;

int min_width(int width[], int start, int end) {
    int res = width[start];
    for (int i=start+1; i<=end; i++) {
        res = res > width[i] ? width[i] : res;
    }
    return res;
}

int main() {
    int size, line_cnt = 0;
    cin >> size >> line_cnt;
    int width[size];
    for (int i=0; i<size; i++) {
        cin >> width[i];
    }
    
    int start, end;
    for (int i=0; i<line_cnt; i++) {
        cin >> start >> end;
        cout << min_width(width, start, end) << endl;
    }
    return 0;
}