function solution(s) {
    var answer = 0;
    let map = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
    for(let i in map){
        s = s.replaceAll(i,map[i])
    }
    answer = s
    return Number(answer);
}