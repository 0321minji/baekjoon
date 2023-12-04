#include<iostream>
#include<cmath>

using namespace std;
const int MAX = 1e6;

int n, number, p[MAX + 1], sss;
char c;
bool z, you;

void fac(int x) {

	sss = (int)sqrt(x);

	for (int i = 2; i <= sss; i++) {
		while (!(x % i)) x /= i, p[i]++;
	}
	if (x > 1) p[x]++;
}

void fac2(int x) {
	sss = (int)sqrt(x);

	for (int i = 2; i <= sss; i++) {
		while (!(x % i)) x /= i, p[i]--;
	}
	if (x > 1) p[x]--;
}

int main() {
	cin.tie(NULL); cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	cin >> n;

	for (int i = 0; i < n; i++) {
		if (!i) {
			cin >> number;
			
			if (number == 0) z = 1;
			else if (number < 0) number *= -1;

			if (number) fac(number);
		}
		else {
			cin >> c >> number;

			if (number == 0) z= 1;
			else if (number < 0) number *= -1;

			if (c == '/') fac2(number);
			else if (number) fac(number);
		}
	}
	if (z) cout << "mint chocolate";
	else {
		for (int i = 2; i <= MAX; i++) {
			if (p[i] < 0) you = 1;
		}
		if (you) cout << "toothpaste";
		else cout << "mint chocolate";
	}
}