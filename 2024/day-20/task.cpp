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
bool vis[200][200];
int distances[200][200];
int N, M, CHEAT_LENGTH = 20;
int baseline, ans = 0;

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

bool inBounds(int y, int x)
{
    return y >= 0 && x >= 0 && y < N && x < M;
}

int calcBaseline(int i, int j, vector<string> &track)
{
    if (!inBounds(i, j) || vis[i][j] || track[i][j] == '#')
        return 1e5;

    if (track[i][j] == 'E')
    {
        distances[i][j] = 0;
        return 0;
    }

    vis[i][j] = 1;
    vi arr = {
        calcBaseline(i + 1, j, track),
        calcBaseline(i - 1, j, track),
        calcBaseline(i, j + 1, track),
        calcBaseline(i, j - 1, track),
    };
    vis[i][j] = 0;
    int ans = 1 + *min_element(all(arr));
    distances[i][j] = ans;
    return ans;
}

void findCheats(int i, int j, vector<string> &track, int dist)
{
    if (!inBounds(i, j) || vis[i][j] || track[i][j] == '#' || track[i][j] == 'E')
        return;

    vis[i][j] = 1;

    rep(k, -CHEAT_LENGTH, CHEAT_LENGTH + 1)
    {
        int remaining = CHEAT_LENGTH - abs(k);
        rep(l, -remaining, remaining + 1)
        {
            if (inBounds(i + k, j + l) && distances[i + k][j + l] + dist + abs(k) + abs(l) + 100 <= baseline)
                ++ans;
        }
    }

    findCheats(i + 1, j, track, dist + 1);
    findCheats(i - 1, j, track, dist + 1);
    findCheats(i, j + 1, track, dist + 1);
    findCheats(i, j - 1, track, dist + 1);
}

int main()
{
    ifstream inputFile(getParentPath() + "/" + file);
    vector<string> track;
    string line;

    while (getline(inputFile, line))
        track.push_back(line);

    N = track.size();
    M = track[0].size();

    rep(i, 0, N)
    {
        memset(vis[i], 0, M);
        rep(j, 0, M) distances[i][j] = 1e5;
    }

    rep(i, 0, N) rep(j, 0, M) if (track[i][j] == 'S')
    {
        baseline = calcBaseline(i, j, track);
        findCheats(i, j, track, 0);
    }

    cout << ans << endl;
}