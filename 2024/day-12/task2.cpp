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

int N, M;
bool vis[200][200];
vector<string> arr;
vector<pii> cornerCombinations = {
    {-1, -1},
    {1, 1},
    {-1, 1},
    {1, -1},
};

bool inBounds(int y, int x)
{
    return y >= 0 && x >= 0 && y < N && x < M;
}

void dfs(int i, int j, int &corners, int &area)
{
    if (vis[i][j])
        return;
    ++area;
    char c = arr[i][j];
    vis[i][j] = 1;
    if (inBounds(i + 1, j) && arr[i + 1][j] == c)
        dfs(i + 1, j, corners, area);
    if (inBounds(i - 1, j) && arr[i - 1][j] == c)
        dfs(i - 1, j, corners, area);
    if (inBounds(i, j + 1) && arr[i][j + 1] == c)
        dfs(i, j + 1, corners, area);
    if (inBounds(i, j - 1) && arr[i][j - 1] == c)
        dfs(i, j - 1, corners, area);

    for (pii e : cornerCombinations)
    {
        if ((!inBounds(i + e.first, j) || arr[i + e.first][j] != c) 
                && (!inBounds(i, j + e.second) || arr[i][j + e.second] != c))
            ++corners;
        if (inBounds(i + e.first, j) 
                && arr[i + e.first][j] == c 
                && inBounds(i, j + e.second) 
                && arr[i][j + e.second] == c 
                && inBounds(i + e.first, j + e.second) 
                && arr[i + e.first][j + e.second] != c)
            ++corners;
    }
}

int main()
{
    ifstream inputFile(getParentPath() + "/" + file);
    string line;
    ll ans = 0;
    while (getline(inputFile, line))
        arr.push_back(line);
    N = arr.size();
    M = arr[0].size();
    rep(i, 0, N) memset(vis[i], 0, M);
    rep(i, 0, N) rep(j, 0, M)
    {
        int corners = 0, area = 0;
        dfs(i, j, corners, area);
        ans += corners * area;
    }
    cout << ans;
}