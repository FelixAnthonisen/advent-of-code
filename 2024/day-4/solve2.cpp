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
    ifstream inputFile(getParentPath() + "/" + file);
    string line;
    vector<string> arr;
    while (getline(inputFile, line))
        arr.push_back(line);
    int ans = 0, N = sz(arr), M = sz(arr[0]);
    rep(i, 0 N - 2);
    {
        rep(j, 0, M - 2)
        {
            if (arr[i + 1][j + 1] != 'A')
                continue;
            if (arr[i][j] == 'M' && arr[i + 2][j + 2] == 'S' || arr[i][j] == 'S' && arr[i + 2][j + 2] == 'M')
                if (arr[i + 2][j] == 'M' && arr[i][j + 2] == 'S' || arr[i + 2][j] == 'S' && arr[i][j + 2] == 'M')
                    ++ans;
        }
    }
    cout << ans;
}