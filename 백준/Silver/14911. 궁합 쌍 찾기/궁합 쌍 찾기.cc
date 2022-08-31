#include<iostream>
#include<algorithm>
#include<map>
#include<vector>

using namespace std;

int findPair(vector<int> arr,int goal) {
	//중복 확인을 위한 map 생성
	map<pair<int, int>, bool> visited;
	
	int result = 0;
	for (int i = 0; i < arr.size(); i++) {
		for (int j = i+1; j < arr.size(); j++) {
			if (arr[i] + arr[j] == goal && !visited.count({ arr[i],arr[j] })) {
				cout<<arr[i]<<" "<<arr[j]<<"\n";
				visited[{arr[i], arr[j]}]=true;
				result++;
			}
		}
	}
	return result;
}
int main(void) {
	vector<int> arr;
	int num;
	//숫자 입력
	while (scanf("%d", &num) !=EOF) {
		arr.push_back(num);
	}
	int goal = arr.back();
	arr.pop_back();

	//오름차순 정렬
	sort(arr.begin(), arr.end());
	cout<<findPair(arr,goal);

}