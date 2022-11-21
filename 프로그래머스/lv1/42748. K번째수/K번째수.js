function solution(array, commands) {
    var answer = [];
    for(let x of commands){
        [i,j,k] = x
        let tmp = array.slice(i-1,j)
        tmp.sort((a,b)=>a-b)
        answer.push(tmp[k-1])
    }
    return answer;
}