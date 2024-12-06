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

bool inBounds(int y, int x, int N, int M)
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
    vector<string> arr;
    while (getline(inputFile, line))
        arr.push_back(line);
    int ans = 0, N = arr.size(), M = arr[0].size(), x, y, dir;
    vector<char> starts = {'>', 'v', '<', '^'};
    rep(i, 0, N)
    {
        rep(j, 0, M)
        {
            char c = arr[i][j];
            if (find(all(starts), c) != starts.end())
            {
                y = i;
                x = j;
                auto it = find(all(starts), c);
                dir = distance(starts.begin(), it);
            }
        }
    }
    rep(i, 0, N)
    {
        rep(j, 0, M)
        {
            if (arr[i][j] != '.')
                continue;
            int pre1 = y, pre2 = x, pre3 = dir;
            arr[i][j] = '#';
            int steps = 0;
            while (1)
            {
                x += dir % 2 ? 0 : dir / 2 ? -1
                                           : 1;
                y += dir % 2 ? dir / 2 ? -1 : 1 : 0;
                if (!inBounds(y, x, N, M))
                    break;
                if (arr[y][x] == '#')
                {
                    x -= dir % 2 ? 0 : dir / 2 ? -1
                                               : 1;
                    y -= dir % 2 ? dir / 2 ? -1 : 1 : 0;
                    ++dir;
                    dir %= 4;
                }
                if (++steps >= N * M)
                {
                    ++ans;
                    break;
                }
            }
            y = pre1;
            x = pre2;
            dir = pre3;
            arr[i][j] = '.';
        }
    }
    cout << ans;
}