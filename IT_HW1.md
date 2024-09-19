#include <iostream>
using namespace std;
char leveling(char c){
    if (('A' <= c) && (c <= 'Z'))
        return(c + 32);
    return(c)
    return(0);
}
int main()
{
    char c;
    do
    {
        cin.get(c);
        cout << leveling(c);
    } while (c != '\n');
    return 0;
}
