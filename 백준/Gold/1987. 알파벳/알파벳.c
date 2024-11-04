#include<stdio.h>
#define MAX(a,b) a>b? a:b

int alpha[26];
int map[20][20];
int result;
int r, c;

void solve(int x, int y, int count) {
	alpha[map[x][y]] = 1;
	result = MAX(result, count);

	int dx[] = { -1, 1, 0, 0 };
	int dy[] = { 0,0,-1,1 };

	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
			if (!alpha[map[nx][ny]]) {
				solve(nx, ny, count + 1);
				alpha [map[nx][ny]]= 0;
			}
		}
	}
}

int main() {
	char str[25];
	scanf("%d %d", &r, &c);

	for (int i = 0; i < r; i++) {
		scanf("%s", str);
		for (int j = 0; j < c; j++) {
			map[i][j] = str[j] - 'A';
		}
	}

	solve(0, 0, 1);
	printf("%d\n", result);
	return 0;
}