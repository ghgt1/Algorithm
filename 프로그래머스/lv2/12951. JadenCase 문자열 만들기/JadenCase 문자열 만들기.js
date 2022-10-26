function solution(s) {
  var answer = "";
  let l1 = s.split("");
  l1.splice(0, 0, " ");
  console.log(l1);
  for (let i = 0; i < l1.length; i++) {
    if (l1[i - 1] === " ") {
      l1[i] = l1[i].toUpperCase();
    } else {
      l1[i] = l1[i].toLowerCase();
    }
  }
    l1[0] = ''
  answer = l1.join("");
  return answer;
}