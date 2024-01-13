#include <vector>
using namespace std;
int solution(vector<vector<int>> sizes) {
    int max_width = 0, max_height = 0;

    for (const auto& size : sizes) {
        int width = (size[0] > size[1]) ? size[0] : size[1];
        int height = (size[0] > size[1]) ? size[1] : size[0];

        if (width > max_width) {
            max_width = width;
        }
        if (height > max_height) {
            max_height = height;
        }
    }
    
    return max_width * max_height;
}