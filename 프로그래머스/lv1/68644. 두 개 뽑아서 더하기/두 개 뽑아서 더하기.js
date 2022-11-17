function solution(numbers) {
    var answer = [];
//     100개중 2개 고르는거. 절대 시간초과 안남
    for(let i=0;i<numbers.length;i++){
        for(let j=0;j<numbers.length;j++){
            if(i!==j){
                if(!answer.includes(numbers[i]+numbers[j])) answer.push(numbers[i]+numbers[j])
            }
        }
    }
    answer.sort((a,b)=>a-b)
    return answer;
}