function solution(n) {
    var answer = 0;
    tmp = String(n);
    for(var i of tmp){
        answer = answer + parseInt(i);
    }
    return answer;
}