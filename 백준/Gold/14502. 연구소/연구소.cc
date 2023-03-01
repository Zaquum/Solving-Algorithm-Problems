#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int n, m; // 행, 열의 크기
int map[8][8]; // 지도 - 0 : 빈 칸, 1 : 벽, 2 : 바이러스
int temp[8][8];
int ans = 0; // 안전 영역의 최대 크기
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

void copyMap() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            temp[i][j] = map[i][j];
        }
    }
}

void spreadVirus(int x, int y) {
    for (int i = 0; i < 4; i++) {
        int tx = x + dx[i];
        int ty = y + dy[i];

        if (tx >= 0 && tx < n && ty >= 0 && ty < m) {
            if (temp[tx][ty] == 0) {
                temp[tx][ty] = 2;
                spreadVirus(tx, ty);
            }
        }
    }
}

void countSafetyZone() {
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (temp[i][j] == 0) count++;
        }
    }
    if (count > ans) ans = count;
}

void makeWall(int x, int y, int cnt) {
    // 벽을 3개 세웠을 때
    if (cnt == 3) {
        copyMap();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (temp[i][j] == 2) spreadVirus(i, j);
            }
        }
        countSafetyZone();
        return;
    }
    
    // 벽 세우기
    for (int i = x; i < n; i++) {
        for (int j = (i == x)? y : 0; j < m; j++) {
            if (map[i][j] == 0) {
                map[i][j] = 1;
                makeWall(i, j, cnt + 1);
                map[i][j] = 0;
            }
        }
    }
}

int main() {
    scanf("%d %d", &n, &m);
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &map[i][j]);
        }
    }
    
    makeWall(0, 0, 0);
    printf("%d\n", ans);
    
    return 0;
}