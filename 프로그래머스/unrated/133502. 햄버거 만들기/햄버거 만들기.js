function solution(ingredient) {
  var answer = 0;
  let stack = [];
  ingredient.forEach((x) => {
    stack.push(x);
    if (stack.length >= 4) {
      if (
        JSON.stringify(stack.slice(stack.length - 4, stack.length)) ===
        JSON.stringify([1, 2,3,1])
      ) {
        answer++;
        stack.pop();
        stack.pop();
        stack.pop();
        stack.pop();
      }
    }
  });
  return answer;
}
