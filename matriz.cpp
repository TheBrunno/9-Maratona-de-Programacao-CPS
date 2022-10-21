#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int matriz[n][n];
    int matriz2[n][n];
    
    for(int i=0;i<n;i++){
        for(int y=0;y<n;y++){
            cin >> matriz[i][y];
        }
    }
    for(int i=0;i<n;i++){
        for(int y=0;y<n;y++){
            cin >> matriz2[i][y];
        }
    }
    for(int i=0;i<n;i++){
        for(int y=0;y<n;y++){
            cout << matriz[i][y] + matriz2[i][y] << " ";
        }
        cout << endl;
    }
    return 0;
}
