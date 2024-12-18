
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
int N = 71, M = 71, X = 1024;

bool inBounds(int y, int x)
{
    return y >= 0 && x >= 0 && y < N && x < M;
}

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
    bool arr[N][M];
    bool vis[N][M];
    rep(i, 0, N)
    {
        memset(arr[i], 0, M);
        memset(vis[i], 0, M);
    }
    vector<pii> cords;
    while (getline(inputFile, line))
    {
        stringstream ss(line);
        int x, y;
        char delimiter;
        ss >> x >> delimiter >> y;
        cords.push_back({x, y});
    }
    rep(i, 0, X) arr[cords[i].second][cords[i].first] = 1;

    queue<vi> q;
    q.push({0, 0, 0});
    while (!q.empty())
    {
        vi v = q.front();
        q.pop();
        int x = v[0], y = v[1], d = v[2];
        if (y == N - 1 && x == M - 1)
        {
            cout << d;
            break;
        }
        if (!inBounds(y, x) || arr[y][x] || vis[y][x])
            continue;
        vis[y][x] = 1;
        q.push({x + 1, y, d + 1});
        q.push({x - 1, y, d + 1});
        q.push({x, y + 1, d + 1});
        q.push({x, y - 1, d + 1});
    }
}