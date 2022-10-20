function solution(s) {
    var answer = '';
    var l1 = s.split(' ')
    for(let i = 0;i<l1.length;i++){
        l1[i] = Number(l1[i])
    }
    function comp(a,b){
        return a-b
    }
    l1.sort(comp)
    answer = `${l1[0]} ${l1[l1.length-1]}`
    return answer;
}