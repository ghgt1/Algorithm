function solution(n) {
    var answer = 0;
//     재귀+메모이제이션
    let map = new Map()
    map.set(0,0n)
    map.set(1,1n)
    for(let i=2;i<=100000;i++){
        map.set(i,(map.get(i-1)+map.get(i-2)))
    
    }
    answer = (map.get(n)%1234567n)
    return Number(answer);
}