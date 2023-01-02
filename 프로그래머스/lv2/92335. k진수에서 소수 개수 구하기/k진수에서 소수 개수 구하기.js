function solution(n, k) {
    function isPrime(num){
        if(num===1) return false
        if(num===2) return true
        for(let i=2;i<=Math.floor(Math.sqrt(num));i++){
            if(num%i===0) return false
        }
        return true
    }
    var answer = 0;
    let a = n.toString(k)
    let l1 = a.split('0')
    console.log(a)
    console.log(l1)
    for(let x of l1){
        if(isPrime(Number(x)) && x!=='') answer++
    }
    return answer;
}