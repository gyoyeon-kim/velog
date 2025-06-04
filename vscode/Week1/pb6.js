/* 직각삼각형 출력하기 */
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input = line.split(" ");
  rl.close();
}).on("close", function () {
  let n = Number(input[0]);
  for (let i = 1; i <= n; i++) {
    console.log("*".repeat(i));
  }
});

/**
 * rl.on('line', function (line) { ... }) : 콘솔에 입력 들어오면 실행되는 이벤트 리스너
 */
