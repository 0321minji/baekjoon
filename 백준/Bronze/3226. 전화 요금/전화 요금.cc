#include<iostream>
#include<string>
using namespace std;

int cal(int h, int m,int time,int charge) {
	int end_h = h;
	int end_m = (m + time) % 60;

	if (m + time >= 60) {
		end_h += 1;
		if (end_h == 24) {
			end_h = 0;
		}
	}
	if (h == 6 && end_h == 7) {
		charge += (time - end_m) * 5 + end_m * 10;
	}
	else if (h == 18 && end_h == 19) {
		charge += (time - end_m) * 10 + end_m * 5;
	}
	else {
		if (6 < h && h < 19) {
			charge += 10 * time;
		}
		else {
			charge += 5 * time;
		}
	}
	return charge;
}

int main() {
	int n, h, m, time;
	int charge = 0;
	string hh;
	cin >> n;
	for (int i = 0; i < n; i++) {
		getline(cin, hh, ':');
		cin >> m >> time;
		charge = cal(stoi(hh), m, time,charge);
	}
	cout << charge;
}