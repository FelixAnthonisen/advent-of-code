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
int mdX = 101, mdY = 103;

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
    ll uL = 0, uR = 0, lL = 0, lR = 0;
    ifstream inputFile(getParentPath() + "/" + file);
    string line;

    while (getline(inputFile, line))
    {
        int px, py, vx, vy;
        std::regex pattern(R"((p|v)=(-?\d+),(-?\d+))");
        std::smatch match;

        for (std::sregex_iterator it(line.begin(), line.end(), pattern), end; it != end; ++it)
        {
            match = *it;
            std::string key = match[1].str();
            int x = std::stoi(match[2].str());
            int y = std::stoi(match[3].str());

            if (key == "p")
            {
                px = x;
                py = y;
            }
            else if (key == "v")
            {
                vx = x;
                vy = y;
            }
        }

        px += vx * 100;
        px = (px % mdX + mdX) % mdX;
        py += vy * 100;
        py = (py % mdY + mdY) % mdY;

        uL += px < mdX / 2 && py < mdY / 2;
        uR += px > mdX / 2 && py < mdY / 2;
        lL += px < mdX / 2 && py > mdY / 2;
        lR += px > mdX / 2 && py > mdY / 2;
    }
    
    cout << uL * uR * lL * lR;
}