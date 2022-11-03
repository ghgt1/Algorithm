function solution(n) {
    var answer = 0;
    var map = new Map()
    map.set(0,0n)
    map.set(1,1n)
    map.set(2,2n)
    for(let i=3;i<=n;i++){
        map.set(i,map.get(i-1)+map.get(i-2))
    }
    answer = map.get(n)%1234567n
    return answer;
}