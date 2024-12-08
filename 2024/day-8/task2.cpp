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
bool inBounds(int y, int x, int N, int M)
{
    return y >= 0 && x >= 0 && y < N && x < M;
}

int main()
{
    ifstream inputFile(getParentPath() + "/" + file);
    string line;
    vector<string> arr;
    while (getline(inputFile, line))
        arr.push_back(line);
    int ans = 0, N = arr.size(), M = arr[0].size();
    bool vis[N][M];
    rep(i, 0, N) memset(vis[i], 0, M);
    rep(i, 0, N) rep(j, 0, M) rep(k, 0, N) rep(l, 0, M)
    {
        if (i == k && j == l)
            continue;
        if (arr[i][j] != arr[k][l] || arr[i][j] == '.' || arr[i][j] == '#')
            continue;
        pii a = {i - k, j - l}, b{k - i, l - j};
        rep(x, 0, N)
        {
            if (!inBounds(i - x * a.first, j - x * a.second, N, M))
                break;
            vis[i - x * a.first][j - x * a.second] = 1;
        }
        rep(x, 0, N)
        {
            if (!inBounds(k - x * b.first, l - x * b.second, N, M))
                break;
            vis[k - x * b.first][l - x * b.second] = 1;
        }
    }
    rep(i, 0, N) rep(j, 0, M) ans += vis[i][j];
    cout << ans;
}