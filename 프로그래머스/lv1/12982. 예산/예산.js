function solution(d, budget) {
    var answer = 0;
    d.sort((a,b)=>a-b)
    d.forEach(x=>{
        if(x<=budget){
            budget = budget-x
            answer++
        }
    })
    return answer;
}