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

bool vis[100][100];
int N, M;

bool inBounds(int y, int x)
{
    return y >= 0 && x >= 0 && y < N && x < M;
}

int dfs(int i, int j, int d, vector<string> &arr)
{
    if (!inBounds(i, j))
        return 0;
    if (arr[i][j] - '0' - d != 1)
        return 0;
    if (vis[i][j])
        return 0;
    vis[i][j] = 1;
    if (arr[i][j] == '9')
        return 1;
    return dfs(i + 1, j, d + 1, arr) + dfs(i - 1, j, d + 1, arr) + dfs(i, j + 1, d + 1, arr) + dfs(i, j - 1, d + 1, arr);
}

int main()
{
    ifstream inputFile(getParentPath() + "/" + file);
    string line;
    vector<string> arr;
    while (getline(inputFile, line))
        arr.push_back(line);
    N = sz(arr);
    M = sz(arr[0]);
    int ans = 0;
    rep(i, 0, N) rep(j, 0, M)
    {
        if (arr[i][j] == '0')
        {
            rep(k, 0, N) memset(vis[k], 0, M);
            ans += dfs(i, j, -1, arr);
        }
    }
    cout << ans;
}