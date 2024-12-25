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
    int ans = 0;
    string line;
    vector<string> lines;
    vector<vi> keys, locks;

    while (getline(inputFile, line))
        lines.push_back(line);

    for (int i = 0; i < sz(lines); i += 8)
    {
        vi item(5);
        rep(j, 0, 7) rep(k, 0, 5)
            item[k] += lines[i + j][k] == '#';
        if (lines[i][0] == '#')
            locks.push_back(item);
        else
            keys.push_back(item);
    }

    for (auto key : keys)
    {
        for (auto lock : locks)
        {
            bool keyFits = 1;
            rep(i, 0, 5)
            {
                if (key[i] + lock[i] > 7)
                {
                    keyFits = 0;
                    break;
                }
            }
            ans += keyFits;
        }
    }

    cout << ans;
}