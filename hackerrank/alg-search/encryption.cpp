#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    string s;
    cin >> s;
    int len = s.length();
    int row, col, d, tmp;
    double sqrt_result;
    sqrt_result = sqrt(len);
    row = floor(sqrt_result);
    col = ceil(sqrt_result);
    d = len - row * col;
    
    if (row*col < len) {
        row++;
    }
    
    for (int i=0; i<col; i++) {
        for (int j=0; j<row; j++) {
            tmp = i + col * j;
            if (tmp >= len) {
                break;
            }
            cout << s[tmp];
        }
        cout << " ";
    }
    cout << endl;
    return 0;
}