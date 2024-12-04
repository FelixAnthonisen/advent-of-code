#include <bits/stdc++.h>
#include <mach-o/dyld.h>
using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

string file = "input.txt";

string getParentPath()
{
    char buffer[PATH_MAX];
    uint32_t size = sizeof(buffer);
    if (_NSGetExecutablePath(buffer, &size) == 0)
    {
        char *lastSlash = strrchr(buffer, '/');
        if (lastSlash != nullptr)
            *lastSlash = '\0';
    }
    return buffer;
}

int main()
{
    ll ans = 0;
    int pre = -1, pre2 = -1;
    vi arr;
    unordered_multiset<int> ms;
    ifstream inputFile(getParentPath() + "/" + file);
    string line;
    while (getline(inputFile, line))
    {
        istringstream stream(line);
        int a, b;
        stream >> a >> b;
        pre = a;
        pre2 = b;
        arr.push_back(a);
        ms.insert(b);
    }
    rep(i, 0, sz(arr))
        ans += ms.count(arr[i]) * arr[i];
    cout << ans;
}
