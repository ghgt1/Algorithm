function solution(n, t, m, p) {
    var answer = '';
    let start = 0
    let count = 0
    let l1 = []
    while(count<=(p+(t-1)*m)){
        let tmp = start.toString(n)
        count += tmp.length
        for(let i=0;i<tmp.length;i++){
            l1.push(tmp[i].toUpperCase())
        }
        start++
    }
    start = p-1
    for(let i=0;i<t;i++){
        answer+=l1[start]
        start+=m
    }
    return answer;
}