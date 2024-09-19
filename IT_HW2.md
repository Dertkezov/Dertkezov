5
#include <iostream>
using namespace std;
int main(){
    int N, X, Y, Z;
    cin >> N >> X >> Y >> Z;
    cout << N - X - Y - Z << endl;
    return(0);
}

6
#include <iostream>
using namespace std;
int main(){
    int Vv, Vm, L, K, N, Xv, Xm;
    cin >> Vv >> Vm >> L >> K >> N;
    Xm = 0;
    Xv = L;
    while ((Xv > Xm) && (Xv < L + K)){
        Xm += Vm;
        if (N > Vv)
            N -= 1;
        else{
            N -= 1;
            Xv += Vv - N;
        }
    }
    if (Xv <= Xm)
        cout << 0;
    else
        cout << N;
}

8
#include <iostream>
using namespace std;
int main(){
    int N, p, res;
    res = 0;
    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> p;
        if (i % 2 == 0)
            res += p;
        else
            res -= p;
    }
    cout << res << endl;
}
