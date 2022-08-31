#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

//문자열 속 숫자 합을 구하는 함수
int sumNum(string str) {
	int sum = 0;
	for (int i = 0; i < str.size(); i++) {
		if (isdigit(str[i])) { //숫자이면
			sum += str[i] - '0'; //char에서 int로 변환
		}
	}
	return sum;
}

//정렬 조건 함수
//const: 상수 선언 키워드
//const와 포인터를 같이 쓰면 포인터가 가리키는 값은 변경X, 주소만 바꿀 수 있음

bool cmp(const string& s1, const string& s2) {
	if (s1.size()!=s2.size()){//두 문자열의 길이가 다르면
		return s1.size() < s2.size(); //길이 짧은 것부터
	}
	if (sumNum(s1) != sumNum(s2)) {//두 문자열 속 숫자 합이 다르다면
		return sumNum(s1) < sumNum(s2); //합이 작은 것부터
	}
	
	return s1 < s2; //사전순 
}

int main() {
	int n;
	vector<string> serial_num;

	//입력
	cin >> n;
	serial_num.assign(n, "");
	//공백을 n번 집어넣는다 (초기화)

	for (int i = 0; i < n; i++) {
		cin >> serial_num[i]; //i번째 원소에 입력값 대입
	}

	//연산 sort함수 활용->cmp 함수 조건에 맞도록 정렬
	sort(serial_num.begin(), serial_num.end(), cmp);

	//출력
	for (int i = 0; i < n; i++) {
		cout << serial_num[i] << '\n';
	}
	return 0;
}