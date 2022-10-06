function solution(n, k) {
    var answer = 0;
    var free = parseInt(n/10)
    answer = 12000*n + (k-free)*2000
    return answer;
}