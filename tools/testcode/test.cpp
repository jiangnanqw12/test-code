#include <iostream>
using namespace std;
void testRe();
int main()
{
    int e;
    testRe();
    return 0;
}
void testRe()
{
    int a = 1;
    int b = 2;
    int &c = a;

    c = 3;
    int d[10] = {0,
                 1,
                 2,
                 3,
                 4};
    for (auto &v : d)
    {
        if (v == 4)
        {
            v = 12;
        }
    }
    cout << d[4];
}