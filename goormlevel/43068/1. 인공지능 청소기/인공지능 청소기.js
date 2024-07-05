// Run by Node.js
// x+y<=n : YES else : NO
function check(input){
	let x=Math.abs(input[0]);
	let y=Math.abs(input[1]);
	let temp=input[2]-(x+y);
	
	if (x+y<=input[2] && temp%2==0){
		return 'YES';
	}
	return 'NO';
}
const readline = require("readline");
var count=0;
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.on("line", function(line) {
	//console.log(line);
	count+=1;
	if(count==1){
		t=line;
	}
	else{
		input=[];
		// console.log(line.trim().split(' '));
		console.log(check(line.trim().split(' ')));
	}
	if (count>t){
		rl.close();
	}
}).on("close", function() {
	process.exit();
});

// rl.on("line", function (x) {
// 	count += 1;
// 	if (count === 1) {
//   	  N = x;
// 	} else {
//   	  input.push(x);
// 	}
//     // 첫 입력에 앞으로 입력할 행의 수(N=x)를 제안받고,
//        나머지는 input 변수에 push
// 	if (count > N) {
//   	  rl.close();
// 	}
// }).on("close", function () {
// 	console.log(input.join(''))
// });