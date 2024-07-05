// // Run by Node.js
// const readline = require('readline');

// (async () => {
// 	let rl = readline.createInterface({ input: process.stdin });
// 	var count=0;
// 	for await (const line of rl) {
// 		//console.log('Hello Goorm! Your input is', line);
// 		input=line.split(' ').map(Number);
// 		if (count==0){
// 			n=input[0]; d=input[1];
// 		}
// 		else{
			
// 			input.sort((a, b) => a - b);
// 			//console.log(input);
// 			// 투 포인터
// 			var start=0; 
// 			var end=0;
// 			var result=0;
		
// 			while (start<n && end<n){
// 				temp=input[end]-input[start];
// 				cnt=(end-start)+1;
// 				//console.log(input,input[end],input[start],temp,start,end);
// 				if (temp<=d){
// 					result=Math.max(cnt,result);
// 					end+=1;
// 				}
// 				else{
// 					start+=1;
// 				}
// 			}
// 			console.log(n-result);
			
// 		}
// 		count+=1;
// 		//console.log(input);
// 		rl.close();
// 	}
	
// 	//process.exit();
// })();
const readline = require('readline');

const sol = (n, limit, arr) => {
	let answer = 0;
	let lp = 0;
	let rp = 0;
	
	arr.sort((a, b) => a - b);
	
	while(lp < n && rp < n){
		const width = arr[rp] - arr[lp];
		const antNum = rp - lp + 1;
		if(width <= limit) {
			answer = Math.max(answer, antNum);
			rp++;
		}
		else if(width > limit) {
			lp++;
		}
	}
	return n - answer;
}

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = []
	
	for await (const line of rl) {
		if(input.length < 2) input.push(line.split(' ').map(Number));
		if(input.length === 2) rl.close();
	}
	console.log(sol(input[0][0], input[0][1], input[1]));
	process.exit();
})();
