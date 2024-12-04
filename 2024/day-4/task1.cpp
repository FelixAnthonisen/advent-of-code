#include <bits/stdc++.h>
#include <mach-o/dyld.h>
using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

string file = "test.txt";

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
    string target = "XMAS";
    rep(i, 0, N)
    {
        rep(j, 0, M)
        {
            if (i + 3 < N)
                ans += string({arr[i][j], arr[i + 1][j], arr[i + 2][j], arr[i + 3][j]}) == target;
            if (i - 3 >= 0)
                ans += string({arr[i][j], arr[i - 1][j], arr[i - 2][j], arr[i - 3][j]}) == target;
            if (j + 3 < M)
                ans += string({arr[i][j], arr[i][j + 1], arr[i][j + 2], arr[i][j + 3]}) == target;
            if (j - 3 >= 0)
                ans += string({arr[i][j], arr[i][j - 1], arr[i][j - 2], arr[i][j - 3]}) == target;
            if (i + 3 < N && j + 3 < M)
                ans += string({arr[i][j], arr[i + 1][j + 1], arr[i + 2][j + 2], arr[i + 3][j + 3]}) == target;
            if (i + 3 < N && j - 3 >= 0)
                ans += string({arr[i][j], arr[i + 1][j - 1], arr[i + 2][j - 2], arr[i + 3][j - 3]}) == target;
            if (i - 3 >= 0 && j + 3 < M)
                ans += string({arr[i][j], arr[i - 1][j + 1], arr[i - 2][j + 2], arr[i - 3][j + 3]}) == target;
            if (i - 3 >= 0 && j - 3 >= 0)
                ans += string({arr[i][j], arr[i - 1][j - 1], arr[i - 2][j - 2], arr[i - 3][j - 3]}) == target;
        }
    }
    cout << ans;
}