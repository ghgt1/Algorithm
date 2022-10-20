function solution(s) {
    var answer = '';
    var l1 = s.split(' ')
    // l1.forEach(i => Number(i))
    function comp(a,b){
        return a-b
    }
    l1.sort(comp)
    answer = `${l1[0]} ${l1[l1.length-1]}`
    return answer;
}