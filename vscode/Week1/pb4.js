/* 아이스 아메리카노 - */
function solution(money) {
  var answer = [];
  answer[0] = Math.floor(money / 5500);
  answer[1] = money % 5500;
  return answer;
}
/**
 * 자바스크립트에서는 append 사용하지 않고 push로 배열안에 값 넣음
 */
