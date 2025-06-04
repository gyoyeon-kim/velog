/* 뒤집힌 문자열 */
function solution(my_string) {
  return my_string.split("").reverse().join("");
}

/**
 * reverse()는 배열에서만 사용 가능
 * 1. split()로 배열로 변경
 * 2. reverse()로 순서 뒤집기
 * 3. join()으로 다시 문자열로 변경
 */
